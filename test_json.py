#!/usr/bin/env pytest

import json
import pytest


def test_json_obj_as_str(json_obj_as_str):
    """Verify that JSON-as-string is valid JSON"""
    single_quote = "'"
    assert single_quote not in json_obj_as_str
    json.loads(json_obj_as_str)


class TestJsonObjAsDict:
    
    def test_json_dumps(self, json_obj_as_dict):
        """Verify that JSON-as-dict can convert to valid JSON"""
        single_quote = "'"
        assert single_quote not in json.dumps(json_obj_as_dict)
    
    @pytest.mark.xfail(reason="str(dict) prints strings with single-quotes")
    def test_str(self, json_obj_as_dict):
        """Confirm that JSON-as-dict __str__() is not valid JSON"""
        single_quote = "'"
        assert single_quote not in str(json_obj_as_dict)
    
    @pytest.mark.xfail(reason="repr(dict) prints strings with single-quotes")
    def test_repr(self, json_obj_as_dict):
        """Confirm that JSON-as-dict __repr__() is not valid JSON"""
        single_quote = "'"
        assert single_quote not in repr(json_obj_as_dict)


def test_json_array_as_str(json_array_as_str):
    """Verify that JSON-as-string is valid JSON"""
    single_quote = "'"
    assert single_quote not in json_array_as_str
    json.loads(json_array_as_str)


class TestJsonArrayAsList:
    
    def test_json_dumps(self, json_array_as_list):
        """Verify that JSON-as-list can convert to valid JSON"""
        single_quote = "'"
        assert single_quote not in json.dumps(json_array_as_list)
    
    @pytest.mark.xfail(reason="str(list) prints strings with single-quotes")
    def test_str(self, json_array_as_list):
        """Confirm that JSON-as-list __str__() is not valid JSON"""
        single_quote = "'"
        assert single_quote not in str(json_array_as_list)
    
    @pytest.mark.xfail(reason="repr(list) prints strings with single-quotes")
    def test_repr(self, json_array_as_list):
        """Confirm that JSON-as-list __repr__() is not valid JSON"""
        single_quote = "'"
        assert single_quote not in repr(json_array_as_list)


def test_json_dumps(json_entity):
    """Verify that json.dumps() converts JSON entity to valid JSON"""
    single_quote = "'"
    result = json.dumps(json_entity)
    assert single_quote not in result
