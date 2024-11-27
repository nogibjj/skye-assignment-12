[![CICD](https://github.com/nogibjj/skye-assignment-12/actions/workflows/CICD.yml/badge.svg)](https://github.com/nogibjj/skye-assignment-12/actions/workflows/CICD.yml)
[![Link to docker image](https://www.docker.com/wp-content/uploads/2023/08/logo-guide-logos-1.svg)](https://hub.docker.com/r/skyea/skye_mini_project_12)
# README

## Project Overview

The purpose of this project is to establish a GitHub Actions workflow that tests across multiple Python versions to ensure the code's stability and compatibility with different environments. This setup leverages GitHub Actions to automate Continuous Integration and Continuous Deployment (CI/CD) processes, ensuring code is tested, formatted, and linted across multiple Python versions. By implementing a build matrix, we can verify that the project functions correctly on Python 3.9, 3.10, 3.11, and 3.12.

## Key Features

- **CI/CD Pipeline**: Automatically triggered on push and pull request events for the `main` branch, or manually via workflow dispatch.
- **Multi-Version Testing**: Utilizes GitHub Actions' matrix strategy to run tests on Python versions 3.9, 3.10, 3.11, and 3.12.
- **Automated Testing and Formatting**: The workflow includes steps to install dependencies, run tests, format code, and lint for code quality checks.

## Workflow Breakdown

1. **Trigger Events**:
   - The workflow runs on every push and pull request targeting the `main` branch.
   - It can also be manually triggered via workflow dispatch.

2. **Jobs**:
   - **Build and Test**:
     - The `build` job runs on the `ubuntu-latest` runner.
     - It uses a matrix to test across multiple Python versions.
     - Steps include checking out the code, setting up Python, installing dependencies via `make install`, and running tests, formatting, and linting with `make test`, `make format`, and `make lint`, respectively.

## Requirements

- **GitHub Actions Workflow**: Set up to test across at least 3 different Python versions using the matrix strategy.
- **Correctly Configured GitHub Actions Matrix**: Ensures the workflow runs efficiently across Python 3.9, 3.10, 3.11, and 3.12.
- **Passing CI/CD**: The workflow ensures that the code is successfully tested, formatted, and linted for each Python version in the matrix.

## Conclusion

This project demonstrates how to set up a robust GitHub Actions CI/CD pipeline with multi-version Python testing. By ensuring compatibility and stability across multiple Python environments, the project maintains high code quality and reliability.
