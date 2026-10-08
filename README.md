# CI/CD Demo: Flask Calculator

![CI](https://github.com/1313rupinder/ci_cd_demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)

A small Flask calculator web app with automated tests and an automated deployment pipeline. Every push is tested on GitHub, and the app goes live only when all tests pass.

**Live demo:** https://ci-cd-demo-jrak.onrender.com

> The app runs on Render's free plan, which sleeps when unused. The first load can take up to a minute.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Tests](#tests)
- [CI/CD Pipeline](#cicd-pipeline)
- [Author](#author)

## About

This project was built to learn and demonstrate CI/CD. The calculator is deliberately simple, so the focus stays on the pipeline: automated testing with GitHub Actions and automated deployment with Render.

## Features

- Addition, subtraction, multiplication and division
- Friendly error message when dividing by zero
- Friendly error message for invalid input
- 9 automated tests that run on every push and pull request
- Automatic deployment after the tests pass

## Tech Stack

| Area | Tool |
|---|---|
| Language | Python 3.12 |
| Web framework | Flask |
| Production server | Gunicorn |
| Testing | pytest |
| CI | GitHub Actions |
| Hosting and CD | Render |

## Project Structure

```text
ci_cd_demo/
|-- .github/
|   `-- workflows/
|       `-- ci.yml          # CI pipeline (GitHub Actions)
|-- templates/
|   `-- index.html          # Calculator page
|-- .gitignore              # Files Git should not track
|-- app.py                  # Flask application
|-- requirements.txt        # Python packages
|-- test_app.py             # Automated tests
`-- README.md               # This file
```

## Getting Started

### Prerequisites

- Git
- Python 3.12

### Installation

```bash
git clone https://github.com/1313rupinder/ci_cd_demo.git
cd ci_cd_demo
python -m pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

Then open http://localhost:8000 in your browser.

### Run the tests

```bash
python -m pytest
```

Expected result: `9 passed`.

## Tests

| Test | What it checks |
|---|---|
| `test_add` | `add(2, 3)` returns 5 |
| `test_is_even` | `is_even` is correct for 4 and 7 |
| `test_home_page_loads` | The home page loads (status 200) and shows "Calculator" |
| `test_calculator_add` | 2 + 3 shows `5.0` |
| `test_calculator_subtract` | 10 - 4 shows `6.0` |
| `test_calculator_multiply` | 6 x 7 shows `42.0` |
| `test_calculator_divide` | 10 / 4 shows `2.5` |
| `test_calculator_divide_by_zero` | Shows "Cannot divide by zero!" and no result |
| `test_calculator_invalid_input` | Shows "Please enter valid numbers." |

## CI/CD Pipeline

```text
git push -> GitHub -> GitHub Actions (install + test) -> Render (deploy) -> Live app
```

### How it works

1. A push to `main` (or a pull request) starts the workflow in `.github/workflows/ci.yml`.
2. GitHub gives the job a fresh Ubuntu machine.
3. The workflow checks out the code, installs Python 3.12 and the packages from `requirements.txt`, then runs `pytest`.
4. If any test fails, the run turns red and the deployment is blocked.
5. If all tests pass, the run turns green and Render deploys the new version.

### Deployment

Deployment is handled by Render, not by a step in the workflow file. Render's Auto-Deploy setting is **After CI Checks Pass**, so a failing check stops the deploy.

This was verified by pushing a broken commit on purpose: CI turned red, Render did not deploy it, and the live site kept the previous version.

## Author

**Rupinder Singh**

- GitHub: [1313rupinder](https://github.com/1313rupinder)
- LinkedIn: [rupinder1313](https://www.linkedin.com/in/rupinder1313)
- 
