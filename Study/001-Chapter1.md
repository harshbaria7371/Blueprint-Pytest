# Chapter 1: The Core Concept (What and Why)

## Section 1.1: What is Pytest and Why Use It? 💡
At its heart, Pytest is a robust, mature, and widely adopted testing framework for the Python programming language. Think of it as the ultimate quality control toolkit for code.

Every piece of software needs checks to ensure it works correctly. While Python has a built-in testing framework called unittest, Pytest has become the industry standard due to its elegance and power.

**Why Pytest is Preferred**
1. Simplicity and Readability: This is Pytest's biggest advantage. It moves away from the verbose, class-based structure of unittest. In Pytest, you write tests using standard Python functions and the native assert keyword.

    - In unittest, you might write: `self.assertEqual(a + b, 5)`
    - In Pytest, you simply write: `assert a + b == 5`

    This drastically reduces boilerplate code, making tests clearer, faster to write, and easier to maintain.
2. Automatic Test Discovery: You don't need to manually tell Pytest where your tests are. It automatically scans directories for files named `test_*.py` or `*_test.py` and looks for functions named `test_*` within those files.
3. Informative Failure Reporting: When a test fails, Pytest provides detailed output, showing you exactly why the assertion failed, including the values of the variables involved. This saves a huge amount of debugging time.

**Analogy**: If writing tests with unittest is like filling out a detailed, multi-page government form every time, using Pytest is like sending a focused text message—you get straight to the point without all the unnecessary formality.

## Section 1.2: Setting Up the First Test File and Running Pytest 💻
Pytest’s true power lies in its **convention over configuration** philosophy. This means it relies on simple naming rules to find and execute your tests automatically, requiring almost zero setup code.

**File and Function Naming Conventions**

Pytest discovers tests based on two key conventions:
- **Test File Name**: Pytest looks for files that start with `test_` or end with `_test.py`
    - *Example*: `test_math.py`, `database_test.py`
- **Test Function Name**: Inside those files, Pytest looks for functions that start with `test_`
    - *Example*: `def test_addition():` or `def test_can_connect_to_db():`

**Writing First Test**

Check the minimal test file in project directory `Study_code/test_001_basic_math.py`. 

With the file saved, open your terminal (make sure you are in the project's root directory) and execute the single command:
```
pytest
```
Pytest will automatically scan your directories, find the `test_basic_math.py` file, execute the two `test_` functions inside it, and report the results. Result should show a clean summary of passed, failed, and skipped tests. 