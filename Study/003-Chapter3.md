# 3. Controlling the Test Run (Markers and Configuration)

## 3.1 Using Markers for Categorization and Skipping

As our test suite grows, we need ways to organize and selectively run subsets of tests. **Markers** are the simple, powerful Pytest mechanism for attaching metadata (tags) to our tests. 

### 1. Categorizing Tests with Custom Markers

Markers allow us to categorize tests as “smoke”, “integration”, “slow” or any other label that makes sense for our project.

We apply a marker using the decorator syntax : @pytest.mark.<marker_name> .
``` Python
import pytest

@pytest.mark.integration
def test_api_connectivity():
	pass
	
@pytest.mark.smoke
def test_application_starts():
	pass
```

**Running Subsets**

The real utility of markers comes when running tests from the command line using `-m` flag:
```
pytest -m smoke

pytest -m "not integration"
```

### 2. Built-in Markers for Test State

Pytest includes two essential built-in markers to manage the state of our tests:

- `@pytest.mark.skip` : This is used to unconditionally skip a test.
    - *When to Use* : If a feature is temporarily broken, if a test is obsolete, or if it only applies to certain operating systems. The test is never executed and is reported as **SKIPPED**.
- `@pytest.mark.xfail` (Expected Failure): This is used for tests that are currently known to fail due to an existing bug, but the test itself is correct.
    - *When to Use* : If we have identified a bug but haven’t fixed it yet, this marker ensures the test still runs, but its failure does **not** count toward the overall test failure count. If it fails, it is reported as **XFAILED**. If it unexpectedly passes (meaning someone fixed the bug), it’s reported as **XPASSED**.

**Analogy:** Markers are like adding specialized labels to packages in a warehouse. You can instantly filter and decide to ship only the "Priority" (smoke) packages, or set aside the "Hold for Repair" (xfail) packages without stopping the entire operation.