from pathlib import Path

# Relative imports
from .config import FilePaths

# Model version
__version__ = "0.01"

# Load storage paths from config.py
file_paths = FilePaths()
api_keys_path = Path(file_paths.api_keys)
ocr_output_path = Path(file_paths.ocr_output)