import pytest
import json
import hashlib
from skeleton_graph import *

def get_hash(object):
    h= hashlib.sha256(json.dumps(object, sort_keys=True).encode())
    return(h.hexdigest())

def test_create_flight_network():
    flight_net = create_flight_network('flight_network.csv', 1)
    assert get_hash(flight_net) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    flight_net = create_flight_network('flight_network.csv', 2)
    assert get_hash(flight_net) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

def test_flight_connection():
    G = create_flight_network('flight_network.csv', 1)
    f = get_flight_connections(G, "Karachi", 'i')
    assert get_hash(f) == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
    fnum = get_number_of_flight_connections(G, "Karachi", 'i')
    assert get_hash(fnum) == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"

def test_flight_details():
    G = create_flight_network('flight_network.csv', 1)
    dur = get_flight_details(G, "Dubai", "Seattle")
    assert get_hash(dur) == "52efd2aad05d27e3eac3665b82f2bffa6da52351ce871c1c28e4ba69b40ea3e6"
    
    G = create_flight_network('flight_network.csv', 2)
    dist = get_flight_details(G, "Dubai", "Seattle")
    assert get_hash(dist) == "7078c7f8564ee0300ee371c8511553483f3465110b7b962bd63822b541aa8892"

def test_add_flight():
    G = create_flight_network('flight_network.csv', 1)
    add_flight(G, "Dubai", "Seattle", 1890)
    assert get_hash(G) == "024bae3271e30538a52d99a5a30b6d9855e5353b6570d5e796791907bcc14916"

def test_add_airport():
    G = create_flight_network('flight_network.csv', 1)
    add_airport(G, "Karachi", "Dubai", 130)
    assert get_hash(G) == "e31412823d06b719a9696d3cd9cde3cc5c1e0871f835eba80e2230230e11ff16"

def test_secondary_flight():
    G = create_flight_network('flight_network.csv', 1)
    fll = get_secondary_flights(G, "Dubai")
    assert get_hash(fll) == "ce4af28792996d4e7a3379b93f38db618de4dff0afe58d27026c07100bda6d73"

def test_common_airpot():
    G = create_flight_network('flight_network.csv', 1)
    c = counting_common_airports(G, "Dubai", "Seattle")
    assert get_hash(c) == "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"

def test_remove_flight():
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Dubai", "Seattle")
    remove_flight(G2, "Dubai", "Seattle")
    assert get_hash(G1) == "ff91b80c37c467fe002bea24ef3b5823fb47b7db0d538db369e80b8c8084d8b3"
    assert get_hash(G2) == "ede372af35310f42e0aa8ba2bee3ee154b5523fcb997bcb04eac5bb79d8c890a"

def test_remove_airport():
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Boston")
    remove_airport(G2, "Boston")
    assert get_hash(G1) == "40bea640fe6cc47ea6b0efbf642d1fd914deee22a8c8d01207d1743885d65479"
    assert get_hash(G2) == "ba3a9eace71539adda0ca4e45c306e57e58b8cfda803d7e792e7cad685775819"

def test_find_all_routes():
    G = create_flight_network('flight_network.csv', 1)
    assert get_hash(find_all_routes(G, "Dubai", "Dubai")) == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"

def test_layovers():
    G = create_flight_network('flight_network.csv', 1)
    assert get_hash(find_number_of_layovers(G, "Dubai", "Seattle")) == "268aebbb0bb20abd1a959c9f0f6299785add2e7c33e709b93489134246003109"
