from my_code import lesson_6

# Set up needed:
# conda install pytest
# ctrl + shift + p > configure tests > pytest > select the tests directory
#

def helper():
    pass

def test_count_returns_correct_list():
    assert ["Number 1", "Number 2"] == lesson_6.count_to(2)