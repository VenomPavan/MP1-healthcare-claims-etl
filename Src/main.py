from extract import extract
from validate import validate
from transform import transform
from load import load
from load_db import load_db
from logger import logger

print("ETL Started")
logger.info("ETL Started")

df = extract()
logger.info(f"Records Extracted: {len(df)}")

validate(df)
logger.info("Validation Passed")

df = transform(df)
logger.info(f"Records After Cleaning: {len(df)}")

load(df)
load_db(df)

logger.info("ETL Completed")

print(df)

print("ETL Completed")