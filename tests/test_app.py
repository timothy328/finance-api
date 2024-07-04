import pytest
from app.app import get_random_decimal, multiply_and_add_json

def test_random_decimal_output_type():
  """Test that random_decimal returns a float."""
  random_number = get_random_decimal()
  assert isinstance(random_number, float)

def test_random_decimal_range():
  """Test that random_decimal returns a value between 0 and 1 (inclusive)."""
  for _ in range(10):
    random_number = get_random_decimal()
    assert -100.0 <= random_number <= 100.0




test_data = [
    (2.5, -3.1, 1.7, 0.1),
    (0, 5, -2, 3),
    (-1.2, 0, 4.8, 3.6),
]

@pytest.mark.parametrize("x, y, z, expected_result", test_data)
def test_multiply_and_add(x, y, z, expected_result):
  """Test that multiply_and_add performs correct multiplication and addition."""
  result = multiply_and_add_json(x, y, z)
  assert result.json['result'] == expected_result