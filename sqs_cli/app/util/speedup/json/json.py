from typing import Any
from ..logger import logger
from ..helpers import try_import_module


# def _default(obj):
#     # if isinstance(obj, BaseModel):
#     #     return obj.dict()
#     raise TypeError()


if try_import_module("orjson"):

    import orjson  # type: ignore

    def loads(s: str) -> Any:
        return orjson.loads(s)

    def dumps(obj: Any) -> str:
        return orjson.dumps(obj).decode()

    logger.debug("Using JSON fast loader: orjson")

elif try_import_module("ujson"):

    import ujson  # type: ignore

    def loads(s: str) -> Any:
        return ujson.loads(s)

    def dumps(obj: Any) -> str:
        return ujson.dumps(obj)

    logger.debug("Using JSON fast loader: ujson")

else:
    import json

    def loads(s: str) -> Any:
        return json.loads(s)

    def dumps(obj: Any) -> str:
        return json.dumps(obj)

    logger.debug("Fast loaders not found. Using default JSON loader")
