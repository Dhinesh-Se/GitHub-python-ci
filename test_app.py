# use playtest to test the app.py file
from app import add 
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

    # add main function here
if __name__ == "__main__":
    test_add()
    print("All tests passed!")