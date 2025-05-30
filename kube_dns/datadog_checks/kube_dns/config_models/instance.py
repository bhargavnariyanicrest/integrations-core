# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class AuthToken(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    reader: Optional[MappingProxyType[str, Any]] = None
    writer: Optional[MappingProxyType[str, Any]] = None


class IgnoreMetricsByLabels(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    target_label_key: Optional[str] = None
    target_label_value_list: Optional[tuple[str, ...]] = None


class TargetMetric(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    label_to_match: Optional[str] = None
    labels_to_get: Optional[tuple[str, ...]] = None


class LabelJoins(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    target_metric: Optional[TargetMetric] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class Proxy(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    http: Optional[str] = None
    https: Optional[str] = None
    no_proxy: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    allow_redirects: Optional[bool] = None
    auth_token: Optional[AuthToken] = None
    auth_type: Optional[str] = None
    aws_host: Optional[str] = None
    aws_region: Optional[str] = None
    aws_service: Optional[str] = None
    bearer_token_auth: Optional[Union[bool, str]] = None
    bearer_token_path: Optional[str] = None
    bearer_token_refresh_interval: Optional[int] = None
    connect_timeout: Optional[float] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    exclude_labels: Optional[tuple[str, ...]] = None
    extra_headers: Optional[MappingProxyType[str, Any]] = None
    headers: Optional[MappingProxyType[str, Any]] = None
    health_service_check: Optional[bool] = None
    health_url: Optional[str] = None
    ignore_metrics: Optional[tuple[str, ...]] = None
    ignore_metrics_by_labels: Optional[IgnoreMetricsByLabels] = None
    ignore_tags: Optional[tuple[str, ...]] = None
    include_labels: Optional[tuple[str, ...]] = None
    kerberos_auth: Optional[str] = None
    kerberos_cache: Optional[str] = None
    kerberos_delegate: Optional[bool] = None
    kerberos_force_initiate: Optional[bool] = None
    kerberos_hostname: Optional[str] = None
    kerberos_keytab: Optional[str] = None
    kerberos_principal: Optional[str] = None
    label_joins: Optional[LabelJoins] = None
    label_to_hostname: Optional[str] = None
    labels_mapper: Optional[MappingProxyType[str, Any]] = None
    log_requests: Optional[bool] = None
    metric_patterns: Optional[MetricPatterns] = None
    metrics: Optional[tuple[Union[str, MappingProxyType[str, str]], ...]] = None
    min_collection_interval: Optional[float] = None
    namespace: Optional[str] = None
    ntlm_domain: Optional[str] = None
    password: Optional[str] = None
    persist_connections: Optional[bool] = None
    prometheus_endpoint: str
    prometheus_metrics_prefix: Optional[str] = None
    prometheus_url: str
    proxy: Optional[Proxy] = None
    read_timeout: Optional[float] = None
    request_size: Optional[float] = None
    send_distribution_buckets: Optional[bool] = None
    send_distribution_counts_as_monotonic: Optional[bool] = None
    send_distribution_sums_as_monotonic: Optional[bool] = None
    send_histograms_buckets: Optional[bool] = None
    send_monotonic_counter: Optional[bool] = None
    send_monotonic_with_gauge: Optional[bool] = None
    service: Optional[str] = None
    skip_proxy: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    timeout: Optional[float] = None
    tls_ca_cert: Optional[str] = None
    tls_cert: Optional[str] = None
    tls_ciphers: Optional[tuple[str, ...]] = None
    tls_ignore_warning: Optional[bool] = None
    tls_private_key: Optional[str] = None
    tls_protocols_allowed: Optional[tuple[str, ...]] = None
    tls_use_host_header: Optional[bool] = None
    tls_verify: Optional[bool] = None
    type_overrides: Optional[MappingProxyType[str, Any]] = None
    use_legacy_auth_encoding: Optional[bool] = None
    use_process_start_time: Optional[bool] = None
    username: Optional[str] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
