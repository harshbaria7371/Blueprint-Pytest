# Blueprint-Pytest
Blueprint-Pytest is an advanced, enterprise-ready test automation framework engineered for high-scale web application validation. It transcends traditional scripting by implementing a "design-first" architecture, ensuring that the test suite remains maintainable, portable, and lightning-fast as the application grows.

## 🏗️ Architectural Foundations
At the heart of Blueprint-Pytest is a strict adherence to Object-Oriented Programming (OOP). By utilizing Abstract Base Classes (ABCs), the framework defines a formal contract for Page Objects and Component models. This ensures that every page in the system follows a predictable structure, centralizing reusable logic (like explicit wait strategies and element interactions) while preventing code duplication.

## 🧪 Intelligent Data Strategy
To solve the "stale data" problem, the framework integrates Faker for dynamic, synthetic data generation. Instead of relying on hard-coded JSON files or database state, Blueprint-Pytest creates realistic, localized test data on-the-fly. This allows for thousands of unique test iterations without the risk of data collisions or environment pollution.

## ⚡ Execution at Scale
Time is the most valuable asset in a CI/CD pipeline. Blueprint-Pytest is optimized for Parallel Execution using pytest-xdist. The framework is architected to be thread-safe, allowing the test suite to be distributed across multiple CPU cores or remote workers, cutting total execution time from minutes to seconds.

## 🐳 Infrastructure-as-Code (IaC)
To eliminate the "works on my machine" syndrome, the entire testing ecosystem is containerized. Using Docker and Docker-Compose, the framework encapsulates the Python runtime, browser drivers, and dependencies into a single, portable unit. The entire environment—from the test runner to the Playwright Grid—can be orchestrated with a single command: docker-compose up.

# Project Structure

```
blueprint-pytest/
├── config/
│   └── credentials.py              # Configuration and credentials (URLs, usernames, passwords)
├── src/
│   └── pages/
│       ├── login_page.py           # Page Object Model - Login page (Playwright)
│       └── products_page.py        # Page Object Model - Products page (Playwright)
├── tests/
│   ├── unit/                       # Unit tests
│   │   ├── test_login.py          # Login page test cases (Playwright)
│   │   └── test_add_to_cart.py    # Add to cart test cases (Playwright)
│   └── integration/                # Integration tests
├── screenshots/                    # Screenshots captured on test failures (auto-generated)
├── Study/                          # Study materials and documentation
├── Study_code/                     # Sample test code examples
├── conftest.py                     # Global pytest fixtures (Playwright setup, screenshot on failure)
├── pytest.ini                      # Pytest configuration (markers, pythonpath)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── PLAYWRIGHT_INTEGRATION.md       # Playwright integration step-by-step guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+

### Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install Playwright browsers (required for tests):**
```bash
python -m playwright install
```

Or install only specific browsers:
```bash
python -m playwright install chromium    # For Chromium (default)
python -m playwright install firefox     # For Firefox
python -m playwright install webkit      # For WebKit (Safari)
```

**Note:** On Windows, use `python -m playwright` instead of just `playwright` if the command is not recognized.

### Running Tests

**Basic Commands:**
```bash
# Run all tests
pytest

# Run only Playwright tests
pytest -m playwright

# Run specific test file
pytest tests/unit/test_login.py

# Run tests with UI marker
pytest -m ui

# Run tests in parallel (using pytest-xdist)
pytest -n auto
```

**Browser Selection:**
```bash
# Run with specific browser (default: chromium)
pytest -m playwright --browser chromium
pytest -m playwright --browser firefox
pytest -m playwright --browser webkit
```

## 📸 Screenshot on Failure
The framework automatically captures full-page screenshots when tests fail. Screenshots are saved in the `screenshots/` directory with the format: `playwright_{test_name}_{timestamp}.png`

**Why:** Screenshots help debug test failures by showing the exact state of the page when the test failed.

## 🎯 Current Implementation
- **Browser Automation**: Playwright (supports Chromium, Firefox, WebKit)
- **Page Object Model**: Implemented in `src/pages/` using Playwright
- **Test Organization**: Unit tests in `tests/unit/`, Integration tests in `tests/integration/`
- **Configuration**: Centralized in `config/credentials.py`
- **Fixtures**: Playwright `page_with_screenshot` fixture with automatic screenshot on failure in `conftest.py`
- **Test Markers**: Use `@pytest.mark.playwright` to identify Playwright tests

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