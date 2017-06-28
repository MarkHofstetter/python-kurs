import pytest
import steuer

def test_steuer():
    assert(steuer.steuer(40000) == 10080)
    assert(steuer.steuer(11000) == 0)
    assert(steuer.steuer(11001) == 0.25)
    assert(steuer.steuer(18001) == 1750.35)
    assert(steuer.steuer(1000000) == 487880)
    # bug #123
    assert(steuer.steuer(14586) == 896.5)
    assert(steuer.steuer(1000001) == 487880.55)