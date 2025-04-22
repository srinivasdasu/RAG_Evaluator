# tests/test_app.py
from app import add
from app import multiply

def test_add():
    assert add(2, 3) == 5

# def test_multiply():
#     assert multiply(3, 4) == 12

# def test_multiply():
#     assert multiply(3, 4) == 11  # This will FAIL!

