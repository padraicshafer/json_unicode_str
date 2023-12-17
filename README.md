# unicode_str

Unicode handling for JSON representations as a string

## Usage

`unicode_str(response.json())` converts a JSON-like object into a string,
using a `strategy` requeted by the caller to encode unicode characters.

### Examples

```python3
# Use the imported `json` library to convert to string
unicode_str(response.json(), use_jsonlib=True)

# Some encoding strategies used by the python str.encode() method
# See https://docs.python.org/3/library/stdtypes.html#str.encode
# See https://docs.python.org/3/library/codecs.html#error-handlers

# Prints ugly escape characters, but does not lose information
unicode_str(response.json())

# Prints '?' instead of each untranslatable unicode character
unicode_str(response.json(), strategy="replace")

# Skips each untranslatable unicode character
unicode_str(response.json(), strategy="ignore")
```

## Unit Tests

Raw JSON content cannot be directly assigned to a python variable.
JSON elements are generally represented as a string, a dict, or a list.

Conversion of these JSON representations into printable strings may generally
result in string content that is no longer valid JSON content.

This is demonstrated by the tests in `test_json.py`.

```bash
% pytest -s -ra -vv test_json.py

================================================== test session starts ==================================================
platform Python 3.8.17, pytest-7.4.2, pluggy-1.3.0
plugins: anyio-4.0.0, cov-4.1.0, asyncio-0.21.1, mock-3.11.1
asyncio: mode=strict
collected 12 items                                                                                                      

test_json.py::test_json_obj_as_str PASSED
test_json.py::TestJsonObjAsDict::test_json_dumps PASSED
test_json.py::TestJsonObjAsDict::test_str XFAIL (str(dict) prints strings with single-quotes)
test_json.py::TestJsonObjAsDict::test_repr XFAIL (repr(dict) prints strings with single-quotes)
test_json.py::test_json_array_as_str PASSED
test_json.py::TestJsonArrayAsList::test_json_dumps PASSED
test_json.py::TestJsonArrayAsList::test_str XFAIL (str(list) prints strings with single-quotes)
test_json.py::TestJsonArrayAsList::test_repr XFAIL (repr(list) prints strings with single-quotes)
test_json.py::test_json_dumps[json_obj_as_str] PASSED
test_json.py::test_json_dumps[json_obj_as_dict] PASSED
test_json.py::test_json_dumps[json_array_as_str] PASSED
test_json.py::test_json_dumps[json_array_as_list] PASSED

================================================ short test summary info ================================================
XFAIL test_json.py::TestJsonObjAsDict::test_str - str(dict) prints strings with single-quotes
XFAIL test_json.py::TestJsonObjAsDict::test_repr - repr(dict) prints strings with single-quotes
XFAIL test_json.py::TestJsonArrayAsList::test_str - str(list) prints strings with single-quotes
XFAIL test_json.py::TestJsonArrayAsList::test_repr - repr(list) prints strings with single-quotes
============================================= 8 passed, 4 xfailed in 0.03s ==============================================
```

`XFAIL` means that the test failed _as expected_.
The expected reason is printed after each `XFAIL` test.

The `XFAIL` results indicate that printing
a JSON object represented as python dict
(or a JSON array represented as python list)
will create invalid JSON elements.
Both dict.__str__() and dict.__repr__() suround all string values
with single quotes, making them invalid JSON strings. 'list' behaves similarly.

### unicode_str() tests

The Unicode conversion strategies supported by unicode_str()
are tested in `test_json_no_unicode.py` with JSON representations
that contain only ASCII-compatible string values.

The results demonstrate that input strings containing valid JSON
are converted by unicode_str() into strings that are also valid JSON.

When `dict` or `list` representations are used, the resulting strings
are NOT valid JSON elements because of the single quotes (').

```bash
% pytest -s -ra test_json_no_unicode.py

========================================================= test session starts =========================================================
platform Python 3.8.17, pytest-7.4.2, pluggy-1.3.0
plugins: anyio-4.0.0, cov-4.1.0, asyncio-0.21.1, mock-3.11.1
asyncio: mode=strict
collected 36 items                                                                                                                    

test_json_no_unicode.py ........xxxxxxxx........xxxxxxxx.x.x

======================================================= short test summary info =======================================================
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[strict] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[ignore] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[replace] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[backslashreplace] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[surrogateescape] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[xmlcharrefreplace] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[namereplace] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_obj_as_dict[surrogatepass] - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[strict] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[ignore] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[replace] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[backslashreplace] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[surrogateescape] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[xmlcharrefreplace] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[namereplace] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr::test_json_array_as_list[surrogatepass] - str(list) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr_UseJsonLib::test_json_obj_as_dict - str(dict) prints strings with single-quotes
XFAIL test_json_no_unicode.py::TestUnicodeStr_UseJsonLib::test_json_array_as_list - str(list) prints strings with single-quotes
=================================================== 18 passed, 18 xfailed in 0.06s ====================================================
```

The same behavior is seen in `test_json_unicode.py`,
where the JSON representations contain strings with non-ASCII, Unicode values.

```bash
% pytest -s -ra test_json_unicode.py 

========================================================= test session starts =========================================================
platform Python 3.8.17, pytest-7.4.2, pluggy-1.3.0
plugins: anyio-4.0.0, cov-4.1.0, asyncio-0.21.1, mock-3.11.1
asyncio: mode=strict
collected 64 items                                                                                                                    

test_json_unicode.py ........xxxxxxxx........xxxxxxxx.....................x.x........

======================================================= short test summary info =======================================================
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[strict] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[ignore] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[replace] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[backslashreplace] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[surrogateescape] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[xmlcharrefreplace] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[namereplace] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_obj_as_dict[surrogatepass] - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[strict] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[ignore] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[replace] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[backslashreplace] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[surrogateescape] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[xmlcharrefreplace] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[namereplace] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr::test_json_array_as_list[surrogatepass] - str(list) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr_UseJsonLib::test_json_obj_as_dict - str(dict) prints strings with single-quotes
XFAIL test_json_unicode.py::TestUnicodeStr_UseJsonLib::test_json_array_as_list - str(list) prints strings with single-quotes
=================================================== 46 passed, 18 xfailed in 0.09s ====================================================
```

One difference is that Unicode characters were converted to ASCII-printable
characters for all unicode_str() tests acting on `dict` or `list`
representations, unless the requested strategy was
"strict", "surrogateescape", "surrogatepass", or `use_jsonlib=True`.

**All** unicode_str() strategies convert Unicode characters to ASCII-printable
characters when acting on string representations of JSON elements,
unless `use_jsonlib=True`.

### Robust conversion of Unicode JSON representations to valid JSON string

Finally, note that the most robust strategy is to simply use `json.dumps()`
with no extra parameters.

```bash
% pytest -s -rA -vv test_json_unicode.py::test_json_dumps

========================================================= test session starts =========================================================
platform Python 3.8.17, pytest-7.4.2, pluggy-1.3.0 -- /Users/padraic/miniconda3/envs/alshub/bin/python
plugins: anyio-4.0.0, cov-4.1.0, asyncio-0.21.1, mock-3.11.1
asyncio: mode=strict
collected 4 items                                                                                                                     

test_json_unicode.py::test_json_dumps[json_obj_as_str] PASSED
test_json_unicode.py::test_json_dumps[json_obj_as_dict] PASSED
test_json_unicode.py::test_json_dumps[json_array_as_str] PASSED
test_json_unicode.py::test_json_dumps[json_array_as_list] PASSED

=============================================================== PASSES ================================================================
======================================================= short test summary info =======================================================
PASSED test_json_unicode.py::test_json_dumps[json_obj_as_str]
PASSED test_json_unicode.py::test_json_dumps[json_obj_as_dict]
PASSED test_json_unicode.py::test_json_dumps[json_array_as_str]
PASSED test_json_unicode.py::test_json_dumps[json_array_as_list]
========================================================== 4 passed in 0.01s ==========================================================
```
