import logging
from enum import Enum
from pathlib import Path

logger = logging.getLogger(__name__)


class FileFormat(Enum):
    PDF = "pdf"
    UNKNOWN = "unknown"


class FileFormatDetector:
    """Detect file format from file header magic bytes."""

    SIGNATURES: dict[bytes, FileFormat] = {
        b"%PDF": FileFormat.PDF,
    }

    # Read enough bytes to match the longest signature
    HEADER_SIZE = max(len(sig) for sig in SIGNATURES)

    @classmethod
    def detect(cls, file_path: str | Path) -> FileFormat:
        """
        Detect file format by inspecting file header bytes.

        Args:
            file_path: Path to the file to inspect.

        Returns:
            Detected FileFormat or UNKNOWN if detection fails.
        """
        path = Path(file_path)

        try:
            if not path.is_file():
                logger.warning("Path is not a regular file: %s", path)
                return FileFormat.UNKNOWN

            with path.open("rb") as file:
                header = file.read(cls.HEADER_SIZE)

        except OSError as exc:
            logger.warning("Failed to read file header from %s: %s", path, exc)
            return FileFormat.UNKNOWN

        for signature, file_format in cls.SIGNATURES.items():
            if header.startswith(signature):
                return file_format

        return FileFormat.UNKNOWN
