# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-11-27
### Изменено
- Запуск Docker (добавлен флаг --reload)
### Добавлено
- Эндпоинт базовой модели (рефакторинг с использованием модуля `dummy_model`)
- Тесты для базовой модели
- Конфигурация Docker Compose
- **Merged**: Стандартизирован API эндпоинт на `/predict`
- **Merged**: Добавлена обработка ошибок для граничных случаев (Ошибка 500)
- **Merged**: Инфраструктура как код (Terraform)

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
