from search import binary_search, linear_search


def test_linear_search_finds_target():
    assert linear_search([8, 3, 10, 4], 10) == 2


def test_linear_search_returns_minus_one_when_target_is_absent():
    assert linear_search([8, 3, 10, 4], 7) == -1


def test_binary_search_finds_target():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3


def test_binary_search_returns_minus_one_when_target_is_absent():
    assert binary_search([1, 3, 5, 7, 9], 6) == -1


def test_binary_search_handles_an_empty_list():
    assert binary_search([], 7) == -1


def test_binary_search_handles_a_single_element_list():
    assert binary_search([42], 42) == 0


def test_binary_search_handles_duplicate_values():
    values = [1, 2, 2, 2, 5]
    result = binary_search(values, 2)
    assert result != -1
    assert values[result] == 2
