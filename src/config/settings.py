from dataclasses import dataclass
from pathlib import Path

@dataclass
class Config:
    RAW_DATA_PATH: Path = Path("data/raw/BrentOilPrices.csv")
    SAMPLE_SIZE: int = 1000  # Use subset for development
    DRAWS: int = 300
    TUNE: int = 300
