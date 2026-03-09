# Project Structure

This repository starts with a minimal structure intended to keep domain code
separated and shared concerns centralized.

## Directory Tree

```text
app/
  __init__.py
  api/
    __init__.py
  extractors/
    __init__.py
    soil/
      __init__.py
    structural/
      __init__.py
    architectural/
      __init__.py
  preprocessors/
    __init__.py
  resolvers/
    __init__.py
  models/
    __init__.py
  utils/
    __init__.py

tests/
  __init__.py
  unit/
    __init__.py
  integration/
    __init__.py
  fixtures/
    .gitkeep

docs/
  project_structure.md

scripts/
  .gitkeep
```

## Responsibilities

- `app/api`: shared API-facing interfaces and request/response coordination.
- `app/extractors`: domain-specific extraction packages kept isolated by domain.
- `app/preprocessors`: shared preprocessing steps used before domain extraction.
- `app/resolvers`: shared resolution logic that maps or links extracted data.
- `app/models`: shared data models and schemas.
- `app/utils`: shared utility helpers that do not belong to a specific domain.

## Architecture Rule

Domain isolation is strict. Soil-specific code must remain inside
`app/extractors/soil`, structural-specific code must remain inside
`app/extractors/structural`, and architectural-specific code must remain inside
`app/extractors/architectural`.

Shared code must live only in `app/utils`, `app/resolvers`,
`app/preprocessors`, `app/models`, or `app/api`. Do not import soil-specific
code into structural or architectural modules.
