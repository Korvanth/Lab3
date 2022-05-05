import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 122, 21]
    test_arr = [11, 12, 21, 22, 25, 34, 64, 90, 100, 122]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 122, 21]
    test_arr = [122, 100, 90, 64, 34, 25, 22, 21, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 122, 21]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])



