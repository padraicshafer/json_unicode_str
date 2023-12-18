import pytest


@pytest.fixture
def json_obj_as_str():
    return '{"str_property": "value_1", "int_property": 2}'


@pytest.fixture
def json_obj_as_dict():
    return {"str_property": "value_1", "int_property": 2}


@pytest.fixture(params=("json_obj_as_str", "json_obj_as_dict"))
def json_obj(request: pytest.FixtureRequest):
    return request.getfixturevalue(request.param)


@pytest.fixture
def json_array_as_str():
    return '["value_1", 2, 3.0, false, null]'


@pytest.fixture
def json_array_as_list():
    return ["value_1", 2, 3.0, False, None]


@pytest.fixture(params=("json_array_as_str", "json_array_as_list"))
def json_array(request: pytest.FixtureRequest):
    return request.getfixturevalue(request.param)


@pytest.fixture(params=(
    "json_obj_as_str", "json_obj_as_dict",
    "json_array_as_str", "json_array_as_list",
))
def json_entity(request: pytest.FixtureRequest):
    return request.getfixturevalue(request.param)
