import json
from types import SimpleNamespace
from test.constants import ANARCHY_RESULT, AZTEC_RESULT, BARRACKS_RESULT, EAGLE_WARRIOR_RESULT, GARLAND_WARS_RESULT, GOTH_RESULT, HERESY_RESULT, HUSKARL_RESULT, JAGUAR_WARRIOR_RESULT, KOREANS_RESULT, PERFUSION_RESULT, TEST_FULL_URL, TEST_URL, TEST_VERSION, TURTLE_SHIP_RESULT, UNIQUE_UNIT_INPUT_SINGLE, WAR_WAGON_RESULT
import pytest
from pythonaoe2 import aoe2
from pytest import raises
import requests
import responses

#TODO Create tests for other calls pass/fail

@responses.activate
def test_civilization404():
    responses.add(responses.GET,
    TEST_FULL_URL + '/civilization/nothing',
    status=404)

    with pytest.raises(requests.exceptions.RequestException):
        resp = aoe2.Client(TEST_URL, TEST_VERSION).get_civilization("nothing")

@responses.activate
def test_civilization():
    responses.add(responses.GET,
    TEST_FULL_URL + '/civilization/Aztecs',
    json=AZTEC_RESULT, status=200)

    responses.add(responses.GET,
    TEST_FULL_URL + '/unit/jaguar_warrior',
    json=JAGUAR_WARRIOR_RESULT, status=200)

    responses.add(responses.GET,
    TEST_FULL_URL + '/technology/garland_wars',
    json=GARLAND_WARS_RESULT, status=200)

    resp = aoe2.Client(TEST_URL, TEST_VERSION)
    data = resp.get_civilization("Aztecs")

    assert data.name == "Aztecs"
    assert "age.api" not in data.unique_unit
    assert "age.api" not in data.unique_tech
    assert resp.get_technology(data.unique_tech[0]).name == "Garland Wars"
    assert resp.get_unit(data.unique_unit[0]).name == "Jaguar Warrior"

@responses.activate
def test_units404():
    responses.add(responses.GET,
    TEST_FULL_URL + 'units/nothing',
    status=404)

    with pytest.raises(requests.exceptions.RequestException):
        resp = aoe2.Client(TEST_URL, TEST_VERSION).get_unit("nothing")

@responses.activate
def test_unit():
    responses.add(responses.GET,
    TEST_FULL_URL + '/unit/Eagle_Warrior',
    json=EAGLE_WARRIOR_RESULT, status=200)

    resp = aoe2.Client(TEST_URL, TEST_VERSION).get_unit("Eagle_Warrior")

    assert resp.name == "Eagle Warrior"
    assert "age.api" not in resp.created_in

@responses.activate
def test_structure404():
    responses.add(responses.GET,
    TEST_FULL_URL + 'structure/nothing',
    status=404)

    with pytest.raises(requests.exceptions.RequestException):
        resp = aoe2.Client(TEST_URL, TEST_VERSION).get_structure("nothing")

@responses.activate
def test_structure():
    responses.add(responses.GET,
    TEST_FULL_URL + '/structure/Barracks',
    json=BARRACKS_RESULT, status=200)

    resp = aoe2.Client(TEST_URL, TEST_VERSION).get_structure("Barracks")

    assert len(resp) == 4
    assert resp[0].name == "Barracks"
    assert resp[3].age =="Imperial"

@responses.activate
def test_technoloy404():
    responses.add(responses.GET,
    TEST_FULL_URL + 'technology/nothing',
    status=404)

    with pytest.raises(requests.exceptions.RequestException):
        resp = aoe2.Client(TEST_URL, TEST_VERSION).get_technology("nothing")

@responses.activate
def test_technology():
    responses.add(responses.GET,
    TEST_FULL_URL + '/technology/Heresy',
    json=HERESY_RESULT, status=200)

    resp = aoe2.Client(TEST_URL, TEST_VERSION).get_technology("Heresy")

    assert resp.name == "Heresy"
    assert resp.applies_to[0] == "Monks"
    assert "age.api" not in resp.develops_in
    assert "age.api" not in resp.applies_to[0]

@responses.activate
def test_recursive_civ_unique_unit_multiple():
    responses.add(responses.GET,
    TEST_FULL_URL + '/unit/war_wagon',
    json=WAR_WAGON_RESULT, status=200)

    responses.add(responses.GET,
    TEST_FULL_URL + '/unit/turtle_ship',
    json=TURTLE_SHIP_RESULT, status=200)

    data = SimpleNamespace(**KOREANS_RESULT)
    resp = aoe2.Client(TEST_URL, TEST_VERSION)._recurse_civ_unit(data)

    assert resp[0] == "war_wagon"
    assert resp[1] == "turtle_ship"

@responses.activate
def test_recursive_civ_unique_technology_multiple():
    responses.add(responses.GET,
    TEST_FULL_URL + '/technology/anarchy',
    json=ANARCHY_RESULT, status=200)

    responses.add(responses.GET,
    TEST_FULL_URL + '/unit/huskarl',
    json=HUSKARL_RESULT, status=200)

    responses.add(responses.GET,
    TEST_FULL_URL + '/technology/perfusion',
    json=PERFUSION_RESULT, status=200)

    data = SimpleNamespace(**GOTH_RESULT)
    resp = aoe2.Client(TEST_URL, TEST_VERSION)._recurse_civ_tech(data)

    assert resp[0] == "anarchy"
    assert resp[1] == "perfusion"

