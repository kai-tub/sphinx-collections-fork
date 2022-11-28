"""
Pytest conftest module containing common test configuration and fixtures.
"""

# See: https://github.com/sphinx-doc/sphinx/issues/7008

import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"
