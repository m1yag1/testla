# testla

FOSS Test Case Management

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for package management.

```bash
# Clone the repository
git clone https://github.com/m1yag1/testla.git
cd testla

# Install dependencies
uv sync

# Install in development mode
uv pip install -e .
```

## Development

### Setup

1. Install development dependencies:
   ```bash
   uv sync --group dev
   ```

2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
# Run tests
tox

# Run tests with coverage
tox -e coverage

# Run specific test environment
tox -e py312
```

### Code Quality

```bash
# Format and lint code
tox -e fix

# Type checking
tox -e mypy

# Run all pre-commit hooks
pre-commit run --all-files
```

## Usage

After installation, you can use the CLI:

```bash
testla --help
```

## Project Structure

```
testla/
├── src/
│   └── testla/
│       ├── __init__.py
│       ├── cli.py
│       └── ...
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
├── pyproject.toml
├── tox.ini
├── README.md
└── ...
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure they pass (`tox`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License
This project is licensed under the Apache-2.0 License - see the LICENSE file for details.

## Author

- m1yag1 - 8730430+m1yag1@users.noreply.github.com
