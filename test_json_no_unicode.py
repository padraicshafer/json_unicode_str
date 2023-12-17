#!/usr/bin/env pytest

import json
import pytest

from unicode_str import unicode_str
from unicode_str import UNICODE_ERROR_STRATEGIES


class TestUnicodeStr:
    """Test unicode_str() with various encoding strategies"""

    @pytest.mark.parametrize("strategy", UNICODE_ERROR_STRATEGIES)
    def test_json_obj_as_str(self, json_obj_as_str, strategy):
        """Verify that unicode_str(valid JSON object) is valid JSON"""
        single_quote = "'"
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

    @pytest.mark.parametrize("strategy", UNICODE_ERROR_STRATEGIES)
    def test_json_array_as_str(self, json_array_as_str, strategy):
        """Verify that unicode_str(valid JSON array) is valid JSON"""
        single_quote = "'"
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


class TestUnicodeStr_UseJsonLib:
    """Test unicode_str() with use_jsonlib=True"""

    def test_json_obj_as_str(self, json_obj_as_str):
        """Verify that unicode_str(valid JSON object) is valid JSON"""
        single_quote = "'"
        result = unicode_str(json_obj_as_str, use_jsonlib=True)
        assert single_quote not in result
        json.loads(json_obj_as_str)

    @pytest.mark.xfail(reason="str(dict) prints strings with single-quotes")
    def test_json_obj_as_dict(self, json_obj_as_dict):
        """Verify that unicode_str(invalid JSON object) is not valid JSON"""
        single_quote = "'"
        result = unicode_str(json_obj_as_dict, use_jsonlib=True)
        assert single_quote not in result
        json.loads(json_obj_as_dict)

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
