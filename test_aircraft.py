import pytest
from AircraftClass import Aircraft

def test_aircraft_initialization_sets_attributes():
    plane = Aircraft("Boeing", 100)
    assert plane.model == "Boeing"
    assert plane.capacity == 100
    assert len(plane.passengers) == 0

def test_boarding_single_passenger():
    plane = Aircraft("Boeing", 2)
    plane.board_passenger("Muath")
    assert plane.passenger_count() == 1
    assert plane.passengers == ["MUATH"]

def test_boarding_multiple_passengers():
    plane = Aircraft("Airbus", 3)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    plane.board_passenger("Layla")
    assert plane.passenger_count() == 3
    assert plane.passengers == ["SARA", "MUATH", "LAYLA"]

def test_boarding_multiple_passengers():
    plane = Aircraft("Airbus", 3)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    plane.board_passenger("Layla")
    assert plane.passenger_count() == 3
    assert plane.passengers == ["SARA", "MUATH", "LAYLA"]

def test_boarding_over_capacity():
    plane = Aircraft("Airbus", 2)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    plane.board_passenger("Layla")
    assert plane.passenger_count() == 2
    assert plane.passengers == ["SARA", "MUATH"]

def test_check_the_duplicate_values():
    plane = Aircraft("B787", 2)
    plane.board_passenger("Kalle")
    plane.board_passenger("Kalle")
    assert plane.passenger_count() == 1
    assert plane.passengers == ["KALLE"]

def test_removing_all_passengers():
    plane = Aircraft("B787", 2)
    plane.board_passenger("Kalle")
    plane.board_passenger("Muath")
    plane.clear_passengers()
    assert plane.passenger_count() == 0
    assert plane.passengers == []