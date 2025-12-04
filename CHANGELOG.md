# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-11-27
### Changed
- Docker startup (added --reload)
### Added
- Base model endpoint (refactored to use `dummy_model` module)
- Tests for base model
- Docker Compose configuration
- **Merged**: Standardized API endpoint to `/predict`
- **Merged**: Added error handling for edge cases (500 Error)
- **Merged**: Infrastructure as Code (Terraform)

## [0.2.0] - 2025-11-20
### Changed
- Added `StandardScaler` to the training pipeline to improve model performance.
- Updated model saving path to `model_v0.2.0.pkl`.

## [0.1.0] - 2025-11-20
### Added
- Initial baseline model implementation using Logistic Regression.
- Basic project structure (src, tests, configs).
- CI pipeline with GitHub Actions.
- Dockerfile for API service.
