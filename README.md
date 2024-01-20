
# Python Flask CI/CD Project

This repository contains a simple Python Flask application, demonstrating the implementation of a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions.

## Application Overview

The application serves a "Hello, World!" message. The main objective is to showcase the CI/CD pipeline setup and operation.

### Technologies Used

- [Python Flask](https://flask.palletsprojects.com/) - Web framework.
- [Pytest](https://docs.pytest.org/) - Testing framework.
- [GitHub Actions](https://github.com/features/actions) - CI/CD platform.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure Python and pip are installed on your system:

```bash
python --version
pip --version
```

### Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To start the Flask application:

```bash
python app/app.py
```

The application should now be running at `http://localhost:5000`.

### Running Tests

Execute the unit tests using pytest:

```bash
pytest
```

## CI/CD Pipeline with GitHub Actions

The CI/CD process is defined in `.github/workflows/ci-cd-pipeline.yml` and is triggered on every push or pull request to the `main` branch. The pipeline performs the following tasks:

1. **Checkout Code**: Clones the repository to the runner.
2. **Setup Python**: Sets up the specified Python version.
3. **Install Dependencies**: Installs the necessary packages using pip.
4. **Run Tests**: Executes the unit tests to verify application functionality.

## Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to the Flask team for their excellent web framework.
- Appreciation to the GitHub Actions team for the CI/CD tools.
- Gratitude to all contributors of open-source projects.
