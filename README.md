# extended_knapsack

0-1 knapsack with an additional constraint of maximum number of items used.

## Usage

`pip3 install extended_knapsack`

```python
from extended_knapsack.knapsack import solve

items = [
    {'weight': 4, 'value': 5, 'my-custom-field': 1},
    {'weight': 3, 'value': 4, 'my-custom-field': 2},
    {'weight': 2, 'value': 3, 'my-custom-field': 3},
    {'weight': 1, 'value': 2, 'my-custom-field': 4},
]

result_value, result_items = knapsack(items, 6, 2)
print(result_value)
# 8
print(result_items)
# [
#   {'weight': 4, 'value': 5, 'my-custom-field': 1},
#   {'weight': 2, 'value': 3, 'my-custom-field': 3}
# ]
```
