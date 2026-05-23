import sys
import os
import shutil
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture(autouse=True)
def reset_data():
    shutil.copy("tests/calls_backup.json", "data/calls.json")
    yield