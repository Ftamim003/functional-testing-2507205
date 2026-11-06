# Functional Testing, CI/CD and Live Deployment

**Student ID:** 2507205  
**Project Name:** Functional Testing, CI/CD and Live Deployment  
**Repository:** [functional-testing-2507205](https://github.com/Ftamim003/functional-testing-2507205)

## 1. Project Overview

This project focuses on functional testing of a Python module containing 16 functions. The objective is to develop comprehensive automated tests, achieve 100% line and branch coverage, implement a Continuous Integration and Continuous Deployment (CI/CD) pipeline, and deploy a web application.

The project uses **pytest** for automated testing, **pytest-cov** for coverage measurement, **Ruff** for code linting, and GitHub Actions for CI/CD automation.

## 2. Technologies Used

- Python 3.11
- pytest
- pytest-cov
- Ruff
- Git and GitHub
- GitHub Actions
- HTML, CSS and JavaScript (planned frontend)
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
├── app.py                    # Planned
├── templates/                # Planned
├── static/                   # Planned
└── .github/
    └── workflows/
        └── ci.yml             # Planned
```

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

## 6. Testing Results

The current test suite covers all 16 functions in `target.py`, including valid inputs, boundary conditions, invalid inputs, exception handling and return types.

**Latest successful local test results:**

| Metric | Result |
|---|---:|
| Total tests passed | 137 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Statements covered | 59/59 |
| Branches covered | 26/26 |
| Failed tests | 0 |

The required 100% coverage threshold has been achieved locally.

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

## 9. Continuous Integration and Deployment

**Implementation status:** In progress.

The planned CI/CD pipeline will:

- Run automatically on pushes and pull requests to `main`.
- Execute tests using Python 3.10, 3.11 and 3.12.
- Run Ruff linting.
- Enforce 100% line and branch coverage.
- Upload coverage reports as workflow artifacts.
- Deploy the application only after successful testing.
- Perform smoke tests against the deployed application.

## 10. Web Application

**Implementation status:** Planned.

The web application will provide an interface to execute all 16 functions from `target.py` and display their results or errors.

## 11. Live Deployment

**Platform:** Render (planned)

**Live URL:** To be added after successful deployment.

The deployed application will expose a `/health` endpoint to report the deployed commit SHA.

## 12. GitHub Repository

[https://github.com/Ftamim003/functional-testing-2507205](https://github.com/Ftamim003/functional-testing-2507205)

---

**Academic Project — Functional Testing, CI/CD and Live Deployment**  
**Student ID: 2507205**