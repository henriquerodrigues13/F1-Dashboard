from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

BASE_DIR      = Path(__file__).resolve().parent.parent
RAW_DIR       = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

DATABASE_URL     = os.getenv("DATABASE_URL")
SCHEMA_RAW       = "raw"
SCHEMA_PROCESSED = "processed"