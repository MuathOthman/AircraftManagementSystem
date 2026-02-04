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
    assert plane.passengers == ["Muath"]

def test_boarding_multiple_passengers():
    plane = Aircraft("Airbus", 3)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    plane.board_passenger("Layla")
    assert plane.passenger_count() == 3
    assert plane.passengers == ["Sara", "Muath", "Layla"]

def test_boarding_multiple_passengers():
    plane = Aircraft("Airbus", 3)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    plane.board_passenger("Layla")
    assert plane.passenger_count() == 3
    assert plane.passengers == ["Sara", "Muath", "Layla"]

def test_boarding_over_capacity():
    plane = Aircraft("Airbus", 2)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    plane.board_passenger("Layla")
    assert plane.passenger_count() == 2
    assert plane.passengers == ["Sara", "Muath"]

def test_removing_button():
    plane = Aircraft("Airbus", 2)
    plane.board_passenger("Sara")
    plane.board_passenger("Muath")
    assert plane.passenger_count() == 2
    plane.clear_passengers()
    assert plane.passengers == []
    assert plane.passenger_count() == 1
