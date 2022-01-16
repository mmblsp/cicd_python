from http import server


def search(needle, haystack):
    left = 0
    right = (len(haystack) - 1)

    while left <= right:
        middle = left + (right - left) // 2
        middle_element = haystack[middle]
        if middle_element == needle:
            return middle
        elif middle_element < needle:
            left = middle
        else:
            right = middle
    raise ValueError("Value not in haystack")

# ======= TESTS ==========


def test_search():
    assert search(2, [1, 2, 3, 4, 5, 6]) == 1, \
        'found needle somewhere in the haystack'