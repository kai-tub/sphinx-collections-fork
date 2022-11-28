from sphinx_collections_fork.collections import DRIVERS
from sphinx_collections_fork.drivers import Driver


def register_driver(name, driver_class):
    if not issubclass(driver_class, Driver):
        raise SphinxCollectionsApiError("Given driver class must be a subclass of the main Driver class.")

    try:
        DRIVERS[name] = driver_class
    except KeyError:
        raise SphinxCollectionsApiError("Driver with name {} already exists.".format(name))


class SphinxCollectionsApiError(BaseException):
    pass
