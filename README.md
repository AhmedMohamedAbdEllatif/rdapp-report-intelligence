# rdapp-report-intelligence

Initial repository bootstrap for the `rdapp-report-intelligence` project.

## Status

This repository is currently set up as the starting point for future work.

At this stage, the repository includes the initial Python package structure,
test folders, supporting docs, and Git ignore rules. Application logic,
dependency definitions, and CI are not part of the repository yet.

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

## Notes

- There are currently no dependency installation steps because the repository
  does not yet include dependency management files.
- There are currently no run commands because application code has not been
  added yet.
- Domain-specific extractor code is expected to remain isolated by domain, with
  shared code placed only in the shared application packages.
