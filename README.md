# Blueprint-Pytest
Blueprint-Pytest is an advanced, enterprise-ready test automation framework engineered for high-scale web application validation. It transcends traditional scripting by implementing a "design-first" architecture, ensuring that the test suite remains maintainable, portable, and lightning-fast as the application grows.

## 🏗️ Architectural Foundations
At the heart of Blueprint-Pytest is a strict adherence to Object-Oriented Programming (OOP). By utilizing Abstract Base Classes (ABCs), the framework defines a formal contract for Page Objects and Component models. This ensures that every page in the system follows a predictable structure, centralizing reusable logic (like explicit wait strategies and element interactions) while preventing code duplication.

## 🧪 Intelligent Data Strategy
To solve the "stale data" problem, the framework integrates Faker for dynamic, synthetic data generation. Instead of relying on hard-coded JSON files or database state, Blueprint-Pytest creates realistic, localized test data on-the-fly. This allows for thousands of unique test iterations without the risk of data collisions or environment pollution.

## ⚡ Execution at Scale
Time is the most valuable asset in a CI/CD pipeline. Blueprint-Pytest is optimized for Parallel Execution using pytest-xdist. The framework is architected to be thread-safe, allowing the test suite to be distributed across multiple CPU cores or remote workers, cutting total execution time from minutes to seconds.

## 🐳 Infrastructure-as-Code (IaC)
To eliminate the "works on my machine" syndrome, the entire testing ecosystem is containerized. Using Docker and Docker-Compose, the framework encapsulates the Python runtime, browser drivers, and dependencies into a single, portable unit. The entire environment—from the test runner to the Selenium/Playwright Grid—can be orchestrated with a single command: docker-compose up.

# Project Structure

```
blueprint-pytest/
├── config/
│   └── credentials.py      # Configuration and credentials (URLs, usernames, passwords)
├── src/
│   └── pages/
│       └── login_page.py   # Page Object Model - Login page implementation
├── tests/
│   ├── unit/               # Unit tests
│   │   └── test_login.py  # Login page test cases
│   └── integration/        # Integration tests
├── screenshots/            # Screenshots captured on test failures (auto-generated)
├── Study/                  # Study materials and documentation
├── Study_code/             # Sample test code examples
├── conftest.py             # Global pytest fixtures (WebDriver setup, screenshot on failure)
├── pytest.ini              # Pytest configuration (markers, pythonpath)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Chrome browser installed
- ChromeDriver installed and in PATH

### Installation
```bash
pip install -r requirements.txt
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_login.py

# Run tests with UI marker
pytest -m ui

# Run tests in parallel (using pytest-xdist)
pytest -n auto
```

## 📸 Screenshot on Failure
The framework automatically captures screenshots when tests fail. Screenshots are saved in the `screenshots/` directory with the format: `{test_name}_{timestamp}.png`

## 🎯 Current Implementation
- **WebDriver**: Selenium WebDriver with Chrome
- **Page Object Model**: Implemented in `src/pages/`
- **Test Organization**: Unit tests in `tests/unit/`, Integration tests in `tests/integration/`
- **Configuration**: Centralized in `config/credentials.py`
- **Fixtures**: WebDriver fixture with automatic screenshot on failure in `conftest.py`

## 📋 Future Enhancements (Proposed)
- Abstract Base Classes (ABCs) for Page Objects
- Docker containerization
- CI/CD pipelines (GitHub Actions)
- Faker integration for dynamic test data
- Framework base classes for reusable components

## Remove Pycache folders and files using this command
``` powershell
Get-ChildItem -Path . -Recurse -Include '__pycache__', '*.pyc', '*.pyo' | Remove-Item -Recurse -Force
```