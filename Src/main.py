from extract import extract
from transform import transform
from load import load
from load_db import load_db
from logger import logger

try:

    logger.info("ETL Started")

    df = extract()
    logger.info(f"Records Extracted: {len(df)}")

    df = transform(df)
    logger.info(f"Records After Cleaning: {len(df)}")

    load(df)
    logger.info("Cleaned CSV saved successfully")

    load_db(df)
    logger.info("Data loaded into SQLite successfully")

    logger.info("ETL Completed")

    print(df)

except Exception as e:

    logger.error(f"ETL Failed: {str(e)}")

    print(f"Error: {e}")