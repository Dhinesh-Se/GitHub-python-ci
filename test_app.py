# use playtest to test the app.py file
from app import add 
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():
    from app import subtract
    assert subtract(2, 1) == 1  
    assert subtract(1, 1) == 0
    assert subtract(0, 1) == -1    
def test_multiply():
    from app import multiply
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

    # add main function here
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    print("All tests passed!")