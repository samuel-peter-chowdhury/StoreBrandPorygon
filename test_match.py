from urllib.request import Request, urlopen
import json
import re
import pytest

from Match import Match

def test_standard_game_case():
    match = Match('https://replay.pokemonshowdown.com/sports-gen8nationaldexlegacy-717884.json')
    match.parseData()
    output = match.toString()
    assert 'Kecleon has 0 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Zeraora has 0 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Deoxys-Speed has 0 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Runerigus has 1 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Klefki has 0 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Dedenne has 0 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Mawile-Mega has 3 direct kills, 0 passive kills, and 0 deaths. ' in output
    assert 'Slowbro has 0 direct kills, 0 passive kills, and 0 deaths. ' in output
    assert 'Mandibuzz has 0 direct kills, 1 passive kills, and 0 deaths. ' in output
    assert 'Monferno has 1 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Hattrem has 0 direct kills, 0 passive kills, and 1 deaths. ' in output
    assert 'Rotom-Wash has 1 direct kills, 0 passive kills, and 0 deaths. ' in output

def test_iron_barbs_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677928303.json')
    match.parseData()
    assert 'Ferrothorn has 0 direct kills, 1 passive kills, and 0 deaths.' in match.toString()

def test_rocky_helmet_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677928303.json')
    match.parseData()
    assert 'Melmetal has 0 direct kills, 1 passive kills, and 0 deaths.' in match.toString()

def test_stealth_rocks_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677924177.json')
    match.parseData()
    assert 'Rhyperior has 0 direct kills, 1 passive kills, and 0 deaths.' in match.toString()

def test_spikes_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1682698868.json')
    match.parseData()
    assert 'Klefki has 0 direct kills, 1 passive kills, and 0 deaths.' in match.toString()

def test_toxic_spikes_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1677109286.json')
    match.parseData()
    assert 'Tentacruel has 0 direct kills, 1 passive kills, and 0 deaths.' in match.toString()

def test_magma_storm_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1678676695.json')
    match.parseData()
    assert 'Heatran has 0 direct kills, 1 passive kills, and 0 deaths.' in match.toString()

def test_future_sight_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldex-1678707069.json')
    match.parseData()
    assert 'Hatterene has 1 direct kills, 0 passive kills, and 0 deaths.' in match.toString()

def test_leech_seed_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1681732452.json')
    match.parseData()
    assert 'Ferrothorn has 0 direct kills, 1 passive kills, and 1 deaths.' in match.toString()

def test_weather_damage_case():
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1680375495-nazywfcmf2ntlfegv6544qyjkf6qhtgpw.json')
    match.parseData()
    assert 'Hippowdon has 0 direct kills, 1 passive kills, and 1 deaths.' in match.toString()