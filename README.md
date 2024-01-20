
# CI/CD Flask App with Docker and Kubernetes Integration

This repository contains a simple Python Flask application, demonstrating the implementation of a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions, Docker, and Kubernetes.

## Application Overview

The application is a minimal Flask web app that displays a "Hello, World!" message. The main objective is to showcase the CI/CD pipeline setup, containerization with Docker, and orchestration with Kubernetes.

### Technologies Used

- [Python Flask](https://flask.palletsprojects.com/) - Web framework.
- [Pytest](https://docs.pytest.org/) - Testing framework.
- [Docker](https://www.docker.com/) - Containerization platform.
- [GitHub Actions](https://github.com/features/actions) - CI/CD platform.
- [Kubernetes](https://kubernetes.io/) - Container orchestration.

## Getting Started

These instructions will guide you through getting a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure Python, pip, Docker, and kubectl are installed on your system:

```bash
python --version
pip --version
docker --version
kubectl version
```

### Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application Locally

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

## Docker Integration

The `Dockerfile` in the root directory defines the container image for the application. Build and run the container locally:

```bash
docker build -t flask-app:latest .
docker run -p 5000:5000 flask-app
```

## Kubernetes Integration

Kubernetes manifests in the `k8s` directory define the deployment and service for the application. Apply these manifests to your cluster:

```bash
kubectl apply -f k8s/
```

Ensure you have configured `kubeconfig` correctly to interact with your Kubernetes cluster.

## CI/CD Pipeline

The CI/CD process is defined in `.github/workflows/ci-cd-pipeline.yml` and is triggered on every push or pull request to the `master` branch. The pipeline performs the following tasks:

1. Checkout Code: Clones the repository to the runner.
2. Setup Python: Sets up the specified Python version.
3. Install Dependencies: Installs the necessary packages using pip.
4. Run Tests: Executes the unit tests to verify application functionality.
5. Build Docker Image: Builds a Docker image for the application.
6. Push Docker Image: Pushes the image to a Docker registry (if on the `master` branch).
7. Deploy to Kubernetes: Applies the Kubernetes manifests to deploy the application (if on the `master` branch).

## Contributing

Contributions are what make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to the Flask team for their excellent web framework.
- Appreciation to the GitHub Actions, Docker, and Kubernetes teams for the CI/CD, containerization, and orchestration tools.
- Gratitude to all contributors of open-source projects.
