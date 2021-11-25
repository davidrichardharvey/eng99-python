from fizzbuzz import *

# user input --> max number to hit
# verify_digits
# monkeypatch

# produces output
def test_fizzbuzz_output_3_returns_fizz():
    assert fizzbuzz_output(3) == "Fizz"

def test_fizzbuzz_output_5_returns_buzz():
    assert fizzbuzz_output(5) == "Buzz"

def test_fizzbuzz_output_15_returns_fizzbuzz():
    assert fizzbuzz_output(15) == "FizzBuzz"

def test_fizzbuzz_output_7_returns_7():
    assert fizzbuzz_output(7) == 7