# Configuration

The application configuration is defined in [`app/config.py`](../app/config.py)
using `pydantic-settings`.

## Available Settings

| Variable | Type | Default |
| --- | --- | --- |
| `MAX_CONCURRENT_JOBS` | integer | `4` |
| `LLM_MAX_CALLS` | integer | `10` |
| `LLM_TIMEOUT` | integer | `60` |
| `STORAGE_PATH` | path | `storage` |
| `CACHE_DIR` | path | `.cache` |
| `EXTRACTOR_VERSION` | string | `v1` |

## Loading

Instantiate `Settings` to load configuration:

```python
from app.config import Settings

settings = Settings()
```

`Settings()` reads values from environment variables and, when present, a
`.env` file in the current working directory. If a value is not provided, the
default from `app/config.py` is used.

## Example

Copy values from `.env.example` into a local `.env` file in the working
directory and adjust them as needed:

```dotenv
MAX_CONCURRENT_JOBS=4
LLM_MAX_CALLS=10
LLM_TIMEOUT=60
STORAGE_PATH=storage
CACHE_DIR=.cache
EXTRACTOR_VERSION=v1
```
