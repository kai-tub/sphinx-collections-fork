# from sphinx.testing.util import SphinxTestApp
from sphinx.application import Sphinx
import pytest
from typing import IO


# @pytest.mark.sphinx("html", srcdir="test-something")
@pytest.mark.sphinx("html", testroot="something")
def test_githubpages(app: Sphinx, status: IO, warning: IO):
    app.builder.build_all()
    assert (app.outdir / ".nojekyll").exists()
