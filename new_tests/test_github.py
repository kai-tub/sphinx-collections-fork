# from sphinx.testing.util import SphinxTestApp
from sphinx.application import Sphinx
import pytest
from typing import IO

#
# @pytest.mark.sphinx(testroot='case1')
# def test_case1(app):
#     # app is Sphinx application for case1 sphinx project (`tests/roots/test-case1`)
#     app.build()

# @pytest.mark.sphinx(confoverrides={'master_doc': 'content'})
# def test_confoverrides(app):
#     # a Sphinx application configured with given setting
#     app.build()

# @pytest.mark.sphinx("html", srcdir="test-something")
@pytest.mark.sphinx("html", testroot="something")
def test_githubpages(app: Sphinx, status: IO, warning: IO):
    app.builder.build_all()
    assert (app.outdir / ".nojekyll").exists()
