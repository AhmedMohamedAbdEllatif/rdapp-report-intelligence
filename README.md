# rdapp-report-intelligence

Initial repository bootstrap for the `rdapp-report-intelligence` project,
including a minimal shared configuration module.

## Status

This repository is currently set up as the starting point for future work.

At this stage, the repository includes the initial Python package structure,
shared configuration support, test folders, supporting docs, and Git ignore
rules. Application logic, dependency management files, and CI are not part of
the repository yet.

## Project Structure

The codebase now includes the initial scaffold for application modules, tests,
documentation, and scripts:

```text
app/
tests/
docs/
scripts/
```

The detailed directory layout and architecture guidance are documented in
[`docs/project_structure.md`](docs/project_structure.md).

Shared configuration is defined in [`app/config.py`](app/config.py) and
documented in [`docs/configuration.md`](docs/configuration.md).

## Setup

1. Clone the repository if you do not already have a local copy:

   ```powershell
   git clone https://github.com/AhmedMohamedAbdEllatif/rdapp-report-intelligence.git
   cd rdapp-report-intelligence
   ```

   Or open the existing local repository if it is already cloned.

2. Confirm Git is installed:

   ```powershell
   git --version
   ```

3. Confirm Python is installed:

   ```powershell
   python --version
   ```

4. Create a virtual environment in the repository root:

   ```powershell
   python -m venv .venv
   ```

5. Activate the virtual environment:

   PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   POSIX shell:

   ```bash
   source .venv/bin/activate
   ```

6. Install the minimal packages currently used by the configuration module and
   tests:

   ```powershell
   python -m pip install pydantic-settings python-dotenv pytest
   ```

## Configuration

The repository includes a `pydantic-settings` based `Settings` class in
[`app/config.py`](app/config.py).

1. Copy [`.env.example`](.env.example) to `.env`.
2. Adjust the values for your local environment.
3. Load settings in Python with:

   ```python
   from app.config import Settings

   settings = Settings()
   ```

For the full field reference and defaults, see
[`docs/configuration.md`](docs/configuration.md).

## Testing

Run the unit tests with:

```powershell
python -m pytest
```

## Notes

- The repository still does not include a dependency management file. Install
  the currently required packages manually until one is added.
- There are currently no run commands because application code has not been
  added yet.
- Domain-specific extractor code is expected to remain isolated by domain, with
  shared code placed only in the shared application packages.
