#!/usr/bin/env pytest

import json
import pytest

from contextlib import nullcontext as does_not_raise

from unicode_str import unicode_str
from unicode_str import UNICODE_ERROR_STRATEGIES, is_ascii_friendly


class UnicodeFixtures:
    """Override fixtures to have Unicode values"""

    @pytest.fixture
    def json_obj_as_str(self, json_obj_as_str: str):
        return json_obj_as_str.replace("value_1", "vålüé_1")

    @pytest.fixture
    def json_obj_as_dict(self, json_obj_as_dict: dict):
        return {
            key: value.replace("value_1", "vålüé_1")
            if isinstance(value, str) else value
            for (key, value) in json_obj_as_dict.items()
        }

    @pytest.fixture
    def json_array_as_str(self, json_array_as_str: str):
        return json_array_as_str.replace("value_1", "vålüé_1")

    @pytest.fixture
    def json_array_as_list(self, json_array_as_list: list):
        return [
            value.replace("value_1", "vålüé_1")
            if isinstance(value, str) else value
            for value in json_array_as_list
        ]


def expectation_context(strategy):
    if is_ascii_friendly(strategy):
        return does_not_raise()
    else:
        return pytest.raises(UnicodeEncodeError)


class TestUnicodeStr(UnicodeFixtures):
    """Test unicode_str() with various encoding strategies and Unicode values"""

    @pytest.mark.parametrize("strategy, expectation", zip(
        UNICODE_ERROR_STRATEGIES,
        map(expectation_context, UNICODE_ERROR_STRATEGIES),
    ))
    def test_json_obj_as_str(self, json_obj_as_str, strategy, expectation):
        """Verify that unicode_str(valid JSON object) is valid JSON"""
        single_quote = "'"
        with expectation:
            result = unicode_str(json_obj_as_str, strategy=strategy)
            assert single_quote not in result
        json.loads(json_obj_as_str)

    @pytest.mark.xfail(reason="str(dict) prints strings with single-quotes")
    @pytest.mark.parametrize("strategy", UNICODE_ERROR_STRATEGIES)
    def test_json_obj_as_dict(self, json_obj_as_dict, strategy):
        """Verify that unicode_str(invalid JSON object) is not valid JSON"""
        single_quote = "'"
        result = unicode_str(json_obj_as_dict, strategy=strategy)
        assert single_quote not in result
        json.loads(json_obj_as_dict)

    @pytest.mark.parametrize("strategy, expectation", zip(
        UNICODE_ERROR_STRATEGIES,
        map(expectation_context, UNICODE_ERROR_STRATEGIES),
    ))
    def test_json_array_as_str(self, json_array_as_str, strategy, expectation):
        """Verify that unicode_str(valid JSON array) is valid JSON"""
        single_quote = "'"
        with expectation:
            result = unicode_str(json_array_as_str, strategy=strategy)
            assert single_quote not in result
        json.loads(json_array_as_str)

    @pytest.mark.xfail(reason="str(list) prints strings with single-quotes")
    @pytest.mark.parametrize("strategy", UNICODE_ERROR_STRATEGIES)
    def test_json_array_as_list(self, json_array_as_list, strategy):
        """Verify that unicode_str(invalid JSON array) is not valid JSON"""
        single_quote = "'"
        result = unicode_str(json_array_as_list, strategy=strategy)
        assert single_quote not in result
        json.loads(json_array_as_list)

    @pytest.mark.parametrize("strategy", 
        filter(is_ascii_friendly, UNICODE_ERROR_STRATEGIES),
    )
    def test_json_to_ascii(self, json_entity, strategy):
        """Verify that unicode_str() output has been converted to ascii"""
        result = unicode_str(json_entity, strategy=strategy)
        assert result.isascii()


class TestUnicodeStr_UseJsonLib(UnicodeFixtures):
    """Test unicode_str() with use_jsonlib=True and Unicode values"""

    def test_json_obj_as_str(self, json_obj_as_str):
        """Verify that unicode_str(valid JSON object) is valid JSON"""
        single_quote = "'"
        result = unicode_str(json_obj_as_str, use_jsonlib=True)
        assert single_quote not in result
        json.loads(json_obj_as_str)
        # Unicode string remains unicode in result
        assert not result.isascii()

    @pytest.mark.xfail(reason="str(dict) prints strings with single-quotes")
    def test_json_obj_as_dict(self, json_obj_as_dict):
        """Verify that unicode_str(invalid JSON object) is not valid JSON"""
        single_quote = "'"
        result = unicode_str(json_obj_as_dict, use_jsonlib=True)
        assert single_quote not in result
        json.loads(json_obj_as_dict)
        # Unicode string in dict gets converted to ascii in result
        print(result)
        assert result.isascii()

    def test_json_array_as_str(self, json_array_as_str):
        """Verify that unicode_str(valid JSON array) is valid JSON"""
        single_quote = "'"
        result = unicode_str(json_array_as_str, use_jsonlib=True)
        assert single_quote not in result
        json.loads(json_array_as_str)

    @pytest.mark.xfail(reason="str(list) prints strings with single-quotes")
    def test_json_array_as_list(self, json_array_as_list):
        """Verify that unicode_str(invalid JSON array) is not valid JSON"""
        single_quote = "'"
        result = unicode_str(json_array_as_list, use_jsonlib=True)
        assert single_quote not in result
        json.loads(json_array_as_list)

    def test_json_to_ascii(self, json_entity):
        """Verify that unicode_str() output contains non-ascii characters"""
        result = unicode_str(json_entity, use_jsonlib=True)
        assert not result.isascii()
        assert ascii(result).isascii()


def test_json_dumps(json_entity):
    """Verify that json.dumps() converts Unicode JSON entity to valid ASCII JSON"""
    single_quote = "'"
    result = json.dumps(json_entity)
    assert single_quote not in result
    assert result.isascii()
