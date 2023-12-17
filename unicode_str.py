#!/usr/bin/env python

import json


def unicode_str(
    json_obj, 
    *, 
    use_jsonlib: bool = False, 
    strategy: str = "backslashreplace",
) -> str:
    """Handle unicode characters to avoid UnicodeEncodeError.
    
    use_jsonlib, bool: Use json.dumps if True, otherwise use string methods
    strategy, str: How to handle UnicodeEncodeError; see str.encode(..., errors=strategy)
    """
    if use_jsonlib:
        return json.dumps(json_obj, ensure_ascii=False)
    else:
        return str(json_obj).encode("ascii", strategy).decode()


UNICODE_ERROR_STRATEGIES = (
    # See https://docs.python.org/3/library/codecs.html#error-handlers
    "strict",
    "ignore",
    "replace",
    "backslashreplace",
    "surrogateescape",
    "xmlcharrefreplace",
    "namereplace",
    "surrogatepass",
)


def is_ascii_unfriendly(value):
    return value in (
        "strict",
        "surrogateescape",
        "surrogatepass",
    )


def is_ascii_friendly(value):
    return not is_ascii_unfriendly(value)
