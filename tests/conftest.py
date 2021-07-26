from pathlib import Path
import json

import pytest

from metadatadb_driver_interface.metadatadb import MetadataDb


@pytest.fixture
def arweave_plugin():
    config_path = Path(__file__).parent / "resources/config.ini"
    return MetadataDb(config_path.as_posix()).plugin


@pytest.fixture
def ddo_example():
    ddo_example_path = Path(__file__).parent / "resources/ddo-example.json"
    return json.loads(ddo_example_path.read_text())
