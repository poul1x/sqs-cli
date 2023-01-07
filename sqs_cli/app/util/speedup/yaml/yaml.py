from typing import IO, Any
from ..helpers import try_import_class
from ..logger import logger

if try_import_class("yaml", "CSafeLoader"):
    from yaml import (
        CSafeLoader as Loader,
        CSafeDumper as Dumper,
        load,
        dump,
    )

    logger.debug("Using YAML fast CLoader")

else:
    from yaml import (
        SafeLoader as Loader,
        SafeDumper as Dumper,
        load,
        dump,
    )

    logger.debug("Failed to load fast CLoader. Using YAML slow SafeLoader")


def safe_load(stream: IO) -> Any:
    return load(stream, Loader)


def safe_dump(stream: IO):
    return dump(stream, Dumper)
