import importlib.metadata
import sphinx
# from pkg_resources import parse_version

__version__ = importlib.metadata.version("sphinx_collections_fork")

from sphinx_collections_fork.collections import (
    clean_collections,
    collect_collections,
    execute_collections,
    final_clean_collections,
)
from sphinx_collections_fork.directives.if_collection import (
    CollectionsIf,
    CollectionsIfDirective,
)

import logging
logging.basicConfig()  # Only need to do this once

LOG = logging.getLogger(__name__)

def setup(app):
    """
    Configures Sphinx

    Registers:

    * config values
    * receivers for events
    * directives
    """

    # Registers config options
    app.add_config_value("collections", {}, "html")
    app.add_config_value("collections_target", "_collections", "html")
    app.add_config_value("collections_clean", True, "html")
    app.add_config_value("collections_final_clean", True, "html")

    # Connects handles to events
    app.connect("config-inited", collect_collections)
    app.connect("config-inited", clean_collections)
    app.connect("config-inited", execute_collections)
    app.connect("build-finished", final_clean_collections)

    app.add_node(CollectionsIf)
    app.add_directive("if-collection", CollectionsIfDirective)
    app.add_directive("ifc", CollectionsIfDirective)

    return {"version": VERSION, "parallel_read_safe": True, "parallel_write_safe": True}