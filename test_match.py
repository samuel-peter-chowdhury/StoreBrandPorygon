from urllib.request import Request, urlopen
import json
import re
import pytest

from Match import Match

def test_standard_game_case():
    match = Match('https://replay.pokemonshowdown.com/sports-gen8nationaldexlegacy-717884.json')
    match.parseData()
    with open('test_case_files/test_standard_game.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_iron_barbs_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677928303.json')
    match.parseData()
    with open('test_case_files/test_iron_barbs.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_rocky_helmet_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677928303.json')
    match.parseData()
    with open('test_case_files/test_rocky_helmet.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_stealth_rocks_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677924177.json')
    match.parseData()
    with open('test_case_files/test_stealth_rocks.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_spikes_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1682698868.json')
    match.parseData()
    with open('test_case_files/test_spikes.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_toxic_spikes_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677109286.json')
    match.parseData()
    with open('test_case_files/test_toxic_spikes.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_magma_storm_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1678676695.json')
    match.parseData()
    with open('test_case_files/test_magma_storm.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_future_sight_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1678707069.json')
    match.parseData()
    with open('test_case_files/test_future_sight.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_leech_seed_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1681732452.json')
    match.parseData()
    with open('test_case_files/test_leech_seed.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_weather_damage_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1680375495-nazywfcmf2ntlfegv6544qyjkf6qhtgpw.json')
    match.parseData()
    with open('test_case_files/test_weather_damage.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_indirect_poison_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1680380125-qmzyer5siqimo3xntb5ec9v82e5gugjpw.json')
    match.parseData()
    with open('test_case_files/test_indirect_poison.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')

def test_nickname_with_dash_case():
    match = Match('https://replay.pokemonshowdown.com/sports-gen8nationaldexlegacy-742172.json')
    match.parseData()
    with open('test_case_files/test_nickname_with_dash.txt', 'r') as file:
        data = file.read()
    assert data.replace('\n', '') == match.toStringNoSpace().replace('\n', '')