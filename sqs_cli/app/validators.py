import os
from typing import Optional
from typer import BadParameter


def string(value: Optional[str]):

    if value is None:
        return value

    value = value.strip()
    if len(value) > 0:
        return value

    raise BadParameter("Empty string not allowed")


def positive_int(value: Optional[int]):

    if value is None:
        return None

    if value <= 0:
        raise BadParameter("Positive integer required")

    return value
