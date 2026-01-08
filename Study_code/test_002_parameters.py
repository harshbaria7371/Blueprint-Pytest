import pytest

def cube(x):
    return x * x * x

@pytest.mark.parametrize("input_number, expected_output", [
    (2, 8),
    (-3, -27),
    (0, 0),
    (10, 1000),
])
def test_cubing_function(input_number, expected_output):
    actual_output = cube(input_number)
    print(f"Input: {input_number}, Expected: {expected_output}, Actual: {actual_output}")
    assert actual_output == expected_output