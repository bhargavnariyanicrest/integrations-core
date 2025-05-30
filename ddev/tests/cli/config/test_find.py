# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from ddev.config.file import DDEV_TOML


def test(ddev, config_file):
    result = ddev("config", "find")

    assert result.exit_code == 0, result.output
    assert result.output == f"{config_file.path}\n"


def test_with_overrides(ddev, config_file, overrides_config):
    overrides_config.touch()

    result = ddev("config", "find")

    assert result.exit_code == 0, result.output
    assert result.output == f"{config_file.path}\n----- Overrides applied from {DDEV_TOML}\n"
