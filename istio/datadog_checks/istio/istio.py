# (C) Datadog, Inc. 2018-Present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
from datadog_checks.base import ConfigurationError, OpenMetricsBaseCheck, is_affirmative

from .check import IstioCheckV2
from .constants import BLACKLIST_LABELS
from .legacy_1_4 import LegacyIstioCheck_1_4
from .metrics import ISTIOD_METRICS


class Istio(OpenMetricsBaseCheck):
    """
    This is a legacy implementation that will be removed at some point, refer to check.py for the new implementation.
    """

    DEFAULT_METRIC_LIMIT = 0

    def __init__(self, name, init_config, instances):
        instance = instances[0]

        if instance.get('istio_mesh_endpoint'):
            raise ConfigurationError("istio_mesh_endpoint needs to be configured in a separate instance.")

        # Support additional configured metric mappings
        metrics = instance.get('metrics', []) + [ISTIOD_METRICS]

        # Include default and user configured labels
        exclude_labels = instance.get('exclude_labels', []) + BLACKLIST_LABELS

        instance.update(
            {
                'prometheus_url': instance.get('istiod_endpoint'),
                'namespace': instance.get('namespace', 'istio'),
                'metrics': metrics,
                'metadata_metric_name': 'istio_build',
                'metadata_label_map': {'version': 'tag'},
                'exclude_labels': exclude_labels,
            }
        )

        super(Istio, self).__init__(name, init_config, instances)

    def __new__(cls, name, init_config, instances):
        instance = instances[0]

        if is_affirmative(instance.get('use_openmetrics', False)):
            return IstioCheckV2(name, init_config, instances)
        else:
            if instance.get('istiod_endpoint'):
                return super(Istio, cls).__new__(cls)
            else:
                return LegacyIstioCheck_1_4(name, init_config, instances)
