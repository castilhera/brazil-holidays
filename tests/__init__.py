"""Test package setup for brazil_holidays."""

from pathlib import Path
import sys

# Ensure the src directory is on the import path so ``import brazil_holidays``
# works when tests are executed without installing the package.
SRC_PATH = Path(__file__).resolve().parents[1] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
