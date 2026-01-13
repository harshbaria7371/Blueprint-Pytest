# 4. Advanced Testing Techniques (Mocking and Plugins)

## 4.1 Isolating Tests with the Monkeypatch Fixture 🐒

Unit tests should only test a single unit of code in isolation. This means they should **not** communicate with databases, make API calls over the network, or read/write to the file system. These actions introduce slowness and external points of failure. 

**Mocking** is the solution : replacing real dependencies with simple, controlled, fake objects during the test run.

**The `monkeypatch` Fixture**

Pytest provides a powerful, built-in fixture called `monkeypatch` to easily perform temporary modifications (monkey-patching) to modules, classes, functions, and environment variables. 

**How it Guarantees Isolation**

The core benefit of `monkeypatch` is its safely. It performs the necessary patching (replacement) for the duration of the test, and then **automatically and reliably reverts** the change afterward, ensuring that one test cannot affect the result of another. 

### 1. Mocking Environment Variables

We can use `monkeypatch.setenv()` to create a temporary environment variable that only exists while test is running. 

```python
def test-check_defauly_user(monkeypatch):
	# simulate the environment variable NOT being set
	monkeypatch.delenv("USER_ID", raising=False)
	
	# Assert that the function falls back to a default value
	assert get_user_id() == "anonymous"
```

### 2. Mocking Functions or Methods

We can replace a complex, slow function (like `requests.get` for an API call) with a simple mock function that returns predefined data instantly:

 

```python
import requests

def mock_get_request(url, **kwargs):
	class MockResponse:
		def json(self):
			return {"status":"success", "data": [1,2,3]}
		def status_code(self):
			return 200
	return MockResponse()
	
def test_fetch_remote_data(monkeypatch):
	# Replace the actual requests.get function with our fast mock
	# Syntax: monkeypatch.setattr(module_to_patch, function_name, new_function)
	monkeypatch.setattr(requests, "get", mock_get_request)
	
	# Now, calling the function in application will use the mock
	data = fetch_data_from_api()
	assert len(data) == 3
```

**When to use `monkeypatch` (The Environment Tweak)**

Use `monkeypatch` when you need to change external settings or simple global states that code depends on. It’s perfect for “Environment Configuration”.

- Scenario: Testing “Maintenance Mode”. Imagine app checks an environment variable called `APP_MODE` . If it’s set to “MAINTENANCE”, the app shows a “Down for Repairs” page.
    - Real-World Test: You use `monkeypatch` to set `APP_MODE` to `MAINTENANCE` just for one test to ensure that the redirect logic works correctly, without actually changing your computer’s settings.
- Scenario: Mocking the File System path. If your code looks for a configuration file in `/etc/my_app/config.json` , you can’t easily run that test on a Windows machine.
    - Real-World Test: Use `monkeypatch` to point that path variable to a local folder in your project instead.

## 4.2 Using the Pytest-Mocker Plugin (Advance Mocking)🕵️

For professional grade unit testing, we not only need to replace dependencies but also need to **verify interaction**. Meaning we need to assert that code called the dependency (the mock) correctly, with the right arguments, and the right number of times. 

The `pytest-mock` plugin, once installed (`pip install pytest-mock` ), provides the built-in `mocker` fixture, which is the preferred way to handle advanced mocking in Pytest. It wraps the standard Python `unittest.mock` library, simplifying its usage and guaranteeing automatic cleanup. 

**Key Capabilities of `mocker`** 

The `mocker` fixture provides the full power of mocking, focusing on replacement and verification :

- `mocker.patch(target)` : This replaces the specified function, method, or object with a mock object. The critical difference here is the rich verification methods available on the mock object.
- **Verification Methods**: Once a function is patched, the mock object allows you to assert its usage:
    - `mock_func.assert_called_once()`
    - `mock_func.assert_called_with('arg1', 123)` (Check arguments)
    - `mock_func.call_count` (Check the number of times it was called)

**Example: Verifying Interaction**

Imagine your application sends an email when a user registers. You don’t want to actually send an email during the test, but you *must* ensure the `send_email` function was called correctly. 

```python
# app.py has the real send_email function

# In your test file:
def test_registration_sends_welcome_email(mocker):
    # 1. Patch the function (replace it with a tracking mock)
    mock_email_sender = mocker.patch("app.send_email")
    
    # 2. Act: Run the code that should trigger the call
    register_new_user("Alice", "alice@example.com")
    
    # 3. Assert (Verification): Check how the mock was used
    # Ensure it was called exactly once, and with the correct arguments.
    mock_email_sender.assert_called_once_with(
        to="alice@example.com", 
        subject="Welcome!",
        body=mocker.ANY # This means we don't care about the exact body content
    )
```

The **`mocker`** fixture provides a clean, Pytest-native way to execute these complex assertions, confirming not just *what* happened, but *how* it happened.

**When to use `mocker` (The Behavior Watchdog)**

Use `mocker` (from `pytest-mock` ) when you need to **verify that an action happened** or when you need a ‘Fake’ version of a complex service. This is “Interaction Testing”.

- Scenario: The Credit Card Gatekeeper. You app has a `process_payment()` function that calls a third-party service like Razorpay. You **never** want to charge a real card during a test!
    - Real-World Test: You use `mocker.patch` to replace the real Razorpay `charge` function. You then assert that your code called the fake function with the correct Rupee amount and currency
- Scenario: Sending ‘Welcome’ Emails. When a user signs up, your code calls `send_email()` . You don’t want to spam your inbox every time you run a test.
    - Real-World Test: You replace the email function with a mock. The test passes if your code *tried* to send the email with the correct “To” address, even though no actual email left the server.

## 4.3 The “Power Couple” - Combining Monkeypatch and Mocker 🤝

In a real-world application, a single function often relies on both **environment settings** (like a toggle) and **external services** (like cloud storage). To test such a function properly, you need to use both tools simultaneously.

**The Scenario**: “Secure User Deletion”

We have a function `delete_user_data()` that:

1. **Checks** an environment variable (ENABLE_DELETION) to ensure the feature is turned on.
2. **Calls** an external cloud service to delete files.

**The code example**

Here is how you would write a clean, safe test for this logic:

```python
import pytest
import os
import cloud_service # change with real library for AWS

def delete_user_data(user_id):
	if os.getenv("ENABLE_DELETION") != "true":
		return "Feature Disabled"
		
	cloud_service.wipe_storage(user_id)
	return "Success"
	
# -- Test
def test_delete_user_data_works(monkeypatch, mocker):
	# Step 1 : Monkey patch to change env variable
	monkeypatch.setenv("ENABLE_DELETION", "true")
	
	# Step 2: Moker to create fake cloud service
	mock_wipe = mocker.patch("cloud_service.wipe_storage")
	
	# ACT : Run the function
	result = delete_user_data("user_123")
	
	# Assert
	assert result == "Success"
	
	# Verify the fake cloud servce was actually called with the right ID
	mock_wipe.assert_called_once_with("user_123")
```

**Why this is the “Gold Standard”:**

- **Isolation**: Your test doesn’t depend on your actual computer’s environment variables.
- **Safety**: You can run this test 1,000 times and you will never accidentally delete a single file from the real cloud.
- **Speed**: Because it doesn’t talk to the internet or a database, this test runs in milliseconds.