# 5. Handling Errors and Exceptions

## 5.1 Testing for Expected Errors with `pytest.raises` ⚠️

Good code doesn’t just work; it fails gracefully. If a user tries to divide by zero or upload a file that’s too large, your code should raise a specific **Exception**. As a tester, you need to verify that these exceptions are actually being triggered when they should be.

In Pytest, we use the `pytest.raises` context manager to wrap code that we *expect* to crash.

**How it Works**

Normally, if a line of code in your test raises an exception, the test fails immediately. However, when you use `with pytest.raises(ErrorName):` , you are telling Pytest: “I expect the following block of code to throw this specific error. If it does, the test passes. If it doesn’t throw the error (or throws a different one), the test fails.”

**The Code Example**

Imagine you have a simple function that divides two numbers:

```python
import pytest

def divide(a, b):
	if b == 0:
		raise ValueError("You cannot divide by zero!")
	return a / b
	
# --- THE TEST ---
def test_divide_by_zero_raises_exception():
	# we tell Pytest to watch for a ValueError
	with pytest.raises(ValueError) as excinfo:
		divide(10, 0)
		
	# Optional: You can even check if the error message is correct!
	assert str(excinfo.value) == "You cannot divide by zero!"
```

**Why use `excinfo` ?**

As shown above, `pytest.raises` can capture the error details into a variable (commonly named `excinfo` ). This allows you to inspect the exception object to ensure the error message is user-friendly and accurate.