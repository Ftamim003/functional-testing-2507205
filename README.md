# Functional Testing, CI/CD and Live Deployment

**Student ID:** 2507205  
**Project Name:** Functional Testing, CI/CD and Live Deployment  
**Repository:** [functional-testing-2507205](https://github.com/Ftamim003/functional-testing-2507205)

![Functional Testing CI](https://github.com/Ftamim003/functional-testing-2507205/actions/workflows/ci.yml/badge.svg?branch=main)

## 1. Project Overview

This project focuses on functional testing of a Python module containing 16 functions. The objective is to develop comprehensive automated tests, achieve 100% line and branch coverage, implement a Continuous Integration and Continuous Deployment (CI/CD) pipeline, and deploy a web application.

The project uses **pytest** for automated testing, **pytest-cov** for coverage measurement, **Ruff** for code linting, and GitHub Actions for CI automation.

## 2. Technologies Used

- Python 3.10, 3.11 and 3.12
- pytest
- pytest-cov
- Coverage.py
- Ruff
- Git and GitHub
- GitHub Actions
- HTML, CSS and JavaScript (frontend development)
- Flask (planned backend)
- Render (planned deployment)

## 3. Project Structure

```text
functional-testing-2507205/
│
├── target.py
├── tests/
│   └── test_target.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── ci.yml
```

Additional frontend and deployment files will be added as development progresses.

## 4. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code (recommended)

### Clone the repository

```bash
git clone https://github.com/Ftamim003/functional-testing-2507205.git
cd functional-testing-2507205
```

### Create a virtual environment

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
```

### Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 5. Running the Tests

Run all automated tests:

```bash
python -m pytest -v
```

Run tests with line and branch coverage:

```bash
python -m pytest -v --cov=target --cov-branch --cov-report=term-missing
```

Enforce the required 100% coverage:

```bash
python -m pytest -v --cov=target --cov-branch --cov-fail-under=100
```

Run Ruff linting:

```bash
ruff check target.py tests/
```

## 6. Testing Results

The test suite covers all 16 functions in `target.py`, including valid inputs, boundary conditions, invalid inputs, exception handling and return types.

**Latest successful local test results:**

| Metric | Result |
|---|---:|
| Total tests passed | 137 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Statements covered | 59/59 |
| Branches covered | 26/26 |
| Failed tests | 0 |
| Ruff linting | Passed |

**GitHub Actions CI results:**

The automated CI workflow has successfully completed on all three supported Python versions.

| Python version | CI result |
|---|---|
| Python 3.10 | Passed |
| Python 3.11 | Passed |
| Python 3.12 | Passed |

The required 100% line and branch coverage threshold is enforced by the CI workflow.

## 7. Functions Covered by Tests

The test suite covers the following functions:

1. `is_adult()`
2. `celsius_to_fahrenheit()`
3. `count_vowels()`
4. `invert()`
5. `greet()`
6. `find_max()`
7. `get_price()`
8. `swap()`
9. `common_items()`
10. `is_leap_year()`
11. `to_int()`
12. `divide()`
13. `power()`
14. `square_root()`
15. `factorial()`
16. `average()`

## 8. Suspected Bugs and Observations

The original `target.py` file has not been modified. During testing, the following potential issues were observed:

### 8.1 `greet()` — Unexpected input type

Passing an integer, such as `greet(123)`, raises an `AttributeError` because the implementation attempts to call `.strip()` on the integer.

**Observation:** The function does not explicitly validate the input type.

### 8.2 `is_adult()` — Boolean input

Python treats Boolean values as integers. Therefore, passing `True` or `False` is accepted as an age.

**Observation:** Boolean values may not be meaningful inputs for an age-checking function.

### 8.3 `is_leap_year()` — Boolean input

Similarly, Boolean values are accepted as years because Python treats them as integers.

**Observation:** The function does not explicitly reject Boolean values as invalid years.

These are reported as suspected input-validation issues. The expected behavior for these specific input types is not explicitly defined in the original function requirements.

## 9. Continuous Integration (CI)

**Implementation status: Completed.**

GitHub Actions is configured to automatically execute the following checks:

- Run on every push to `main`.
- Run on pull requests targeting `main`.
- Test using Python 3.10, 3.11 and 3.12.
- Install dependencies from `requirements.txt`.
- Run Ruff linting.
- Execute the complete pytest test suite.
- Enforce 100% line and branch coverage.
- Generate a coverage report in XML format.
- Upload coverage reports as GitHub Actions artifacts.

The CI workflow uses a matrix strategy to verify compatibility across all three Python versions.

## 10. Web Application

**Implementation status: Pending.**

The planned web application will provide an interface to execute all 16 functions from `target.py` and display their results or errors.

The application will use a Flask backend with an HTML, CSS and JavaScript frontend.

## 11. Continuous Deployment and Live Deployment

**Implementation status: Pending.**

**Deployment platform:** Render

The planned deployment pipeline will:

- Deploy only after successful CI testing.
- Deploy automatically when changes are pushed to `main`.
- Use GitHub Secrets for deployment credentials.
- Expose a `/health` endpoint.
- Return the deployed Git commit SHA.
- Display the deployed commit SHA in the frontend.
- Perform smoke tests against the live application.

**Live URL:** To be added after successful deployment.

## 12. GitHub Repository

[View the GitHub Repository](https://github.com/Ftamim003/functional-testing-2507205)

---

**Academic Project — Functional Testing, CI/CD and Live Deployment**  
**Student ID: 2507205**