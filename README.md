# Functional Testing, CI/CD and Live Deployment

**Student ID:** 2507205  
**Project Name:** Functional Testing, CI/CD and Live Deployment  
**GitHub Repository:** [functional-testing-2507205](https://github.com/Ftamim003/functional-testing-2507205)  
**Live Application:** [https://functional-testing-2507205.onrender.com/](https://functional-testing-2507205.onrender.com/)

[![Functional Testing CI](https://github.com/Ftamim003/functional-testing-2507205/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Ftamim003/functional-testing-2507205/actions/workflows/ci.yml)

## 1. Project Overview

This project focuses on functional testing of a Python module containing 16 functions. The main objectives are to develop comprehensive automated tests, achieve 100% line and branch coverage, implement a Continuous Integration and Continuous Deployment (CI/CD) pipeline, and deploy a web application.

The project uses **pytest** for automated testing, **pytest-cov** for coverage measurement, **Ruff** for code linting, Flask for the backend, and GitHub Actions for CI/CD automation.

A web-based interface is also provided to execute all 16 functions and display their results or errors.

## 2. Technologies Used

- Python 3.10, 3.11 and 3.12
- pytest
- pytest-cov
- Coverage.py
- Ruff
- Flask
- Gunicorn
- HTML, CSS and JavaScript
- Git and GitHub
- GitHub Actions
- Render

## 3. Project Structure

```text
functional-testing-2507205/
│
├── target.py
├── app.py
├── tests/
│   ├── test_target.py
│   └── test_app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── ci.yml
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
python -m pytest -v --cov=target --cov-branch --cov-report=term-missing --cov-fail-under=100
```

Run Ruff linting:

```bash
ruff check target.py tests/ app.py
```

## 6. Testing Results

The automated test suite covers all 16 functions in `target.py`, including valid inputs, boundary conditions, invalid inputs, exception handling and return types.

**Latest successful local test results:**

| Metric | Result |
|---|---:|
| Total tests passed | 144 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Statements covered | 59/59 |
| Branches covered | 26/26 |
| Failed tests | 0 |

Ruff linting also passed successfully.

### GitHub Actions CI results

The CI workflow successfully executes tests across all three supported Python versions.

| Python version | CI result |
|---|---|
| Python 3.10 | Passed |
| Python 3.11 | Passed |
| Python 3.12 | Passed |

The CI workflow enforces the required 100% line and branch coverage threshold.

## 7. Functions Covered by Tests

The test suite covers the following 16 functions:

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

### Intentional CI failure demonstration

An intentionally failing test was added to a separate feature branch to demonstrate the CI pipeline's failure detection.

The results demonstrated that:

- All three Python CI jobs failed when the intentional failing test was present.
- After removing the temporary failing test, all three Python CI jobs passed.
- The corrected changes were successfully merged into `main`.

This demonstrated that the CI pipeline detects failing tests and prevents a failing pull request from being merged when the required checks are enforced.

## 10. Web Application

**Implementation status: Completed.**

A Flask-based web application has been developed with an HTML, CSS and JavaScript frontend.

The application provides:

- An interface to select and execute all 16 functions.
- Dynamic input fields based on the selected function.
- Display of successful results and their data types.
- Display of errors and exception information.
- A backend API endpoint for function execution.
- A health endpoint for checking application status and deployed commit information.
- A deployment information section displaying application health and the deployed commit SHA.

### Run the application locally

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

### API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Display the web application |
| POST | `/api/run` | Execute a selected function |
| GET | `/health` | Check application health and deployed commit SHA |

## 11. Continuous Deployment and Live Deployment

**Implementation status: Completed.**

The Flask application is deployed on **Render** using GitHub Actions.

**Live Application:**  
[https://functional-testing-2507205.onrender.com/](https://functional-testing-2507205.onrender.com/)

### Deployment configuration

The application uses Gunicorn as its production WSGI server.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Deployment platform: Render
- Source repository: GitHub

### Deployment pipeline

The GitHub Actions workflow performs the following tasks:

1. Runs automated tests on Python 3.10, 3.11 and 3.12.
2. Executes Ruff linting.
3. Enforces 100% line and branch coverage.
4. Deploys to Render only after successful testing.
5. Deploys only when changes are pushed to the `main` branch.
6. Uses GitHub Secrets to protect deployment credentials.
7. Runs live smoke tests after deployment.

Automatic deployment is disabled on Render so that GitHub Actions controls the deployment process.

### Deployment verification

The `/health` endpoint returns the application health status and deployed Git commit SHA.

The frontend displays the deployed commit SHA to help verify which version is running.

Live endpoints:

- Homepage: [https://functional-testing-2507205.onrender.com/](https://functional-testing-2507205.onrender.com/)
- Health check: [https://functional-testing-2507205.onrender.com/health](https://functional-testing-2507205.onrender.com/health)

The live smoke tests verify the deployed application through HTTP requests, including the homepage, health endpoint and function execution API.

## 12. Branch Protection

**Implementation status: Completed.**

The `main` branch has a GitHub branch protection rule configured with:

- Pull requests required before merging.
- Required CI status checks before merging.
- Branches required to be up to date before merging.

This helps ensure that changes are reviewed through pull requests and pass the required automated checks before merging into `main`.

## 13. GitHub Repository and Live Application

**GitHub Repository:**  
[https://github.com/Ftamim003/functional-testing-2507205](https://github.com/Ftamim003/functional-testing-2507205)

**Live Application:**  
[https://functional-testing-2507205.onrender.com/](https://functional-testing-2507205.onrender.com/)

---

**Academic Project — Functional Testing, CI/CD and Live Deployment**  
**Student ID: 2507205**