from ai_binary_search import binary_search_ai


def test_ai_binary_search_finds_target_in_single_element_list():
    """This test is expected to fail until the AI implementation is fixed."""
    assert binary_search_ai([42], 42) == 0
