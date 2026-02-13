#!/usr/bin/env python3

import sys
import logging
import requests
import pandas as pd
from datetime import datetime
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def extract():
    url = "http://api.open-notify.org/iss-now.json"
    logger.info("Extracting data from API...")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("message") == "success":
        return data
    return None


def transform(data_record):
    logger.info("Transforming data...")
    flat_data = {
        "timestamp": data_record["timestamp"],
        "latitude": data_record["iss_position"]["latitude"],
        "longitude": data_record["iss_position"]["longitude"]
    }
    df = pd.DataFrame([flat_data])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    return df

def load(df, output_file, iteration):
    if df is None:
        return
    try:
        write_header = not iteration > 0
        df.to_csv(output_file, mode='a', index=False, header=write_header)
        logger.info(f"Iteration {iteration + 1}: Data saved to {output_file}")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")

def main():
    output_csv = sys.argv[1]
    for i in range(10):
        logger.info(f"Start looping {i + 1}/10 ---")
        raw_data = extract()
        if raw_data:
            transformed_df = transform(raw_data)
            load(transformed_df, output_csv, i)
        if i < 9:
            logger.info("Waiting...")
            time.sleep(5)

if __name__ == "__main__":
    main()