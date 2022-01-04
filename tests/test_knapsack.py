from hypothesis import given, strategies as st

from src.extended_knapsack.knapsack import solve


@given(
    # items (list of (weight, value) tuples)
    st.lists(st.tuples(
        st.integers(min_value=1),
        st.integers(min_value=1)),
        min_size=0
    ),
    # capacity
    st.integers(min_value=0),
    # max items
    st.integers(min_value=0),
)
def test_num_items(lst, capacity, max_items):
    items = [{'weight': item[0], 'value': item[1]} for item in lst]
    capacity = min(len(items), capacity)
    max_items = min(len(items), max_items)
    result_value, result_items = solve(items, capacity, max_items)
    assert len(result_items) <= max_items
    assert result_value >= 0


def test_from_wikipedia():
    """
    https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
    """
    items = [
        {'weight': 4, 'value': 5},
        {'weight': 3, 'value': 4},
        {'weight': 2, 'value': 3},
        {'weight': 1, 'value': 2},
    ]

    result_value, result_items = solve(items, 6, 4)
    assert result_value == 9
    assert len(result_items) == 3


def test_from_wikipedia_modified():
    items = [
        {'weight': 4, 'value': 5},
        {'weight': 3, 'value': 4},
        {'weight': 2, 'value': 3},
        {'weight': 1, 'value': 2},
    ]

    result_value, result_items = solve(items, 6, 1)
    assert result_value == 5
    assert len(result_items) == 1
