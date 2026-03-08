#!/usr/bin/env python3

import sys
import os
import logging
import requests
import pandas as pd
from datetime import datetime
import time
import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

DB_CONFIG = {'host': os.getenv('DBHOST'), 'user':os.getenv('DBUSER'), 'password':os.getenv('DBPASS'),'database':'iss'}

def register_reporter(table, reporter_id, reporter_name):
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)", 
                           (reporter_id, reporter_name))
        db.commit()
        logger.info(f"Registered reporter: {reporter_name}")
    except mysql.connector.Error as e:
        logger.error(f"Error registering reporter: {e}")
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

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
        "message": data_record.get("message"),
        "timestamp": data_record["timestamp"],
        "latitude": data_record["iss_position"]["latitude"],
        "longitude": data_record["iss_position"]["longitude"]
    }
    df = pd.DataFrame([flat_data])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

def load(df, reporter_id):
    if df is None:
        return
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = """INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id) 
                 VALUES (%s, %s, %s, %s, %s)"""
        row = df.iloc[0]
        values = (row['message'], row['latitude'], row['longitude'], row['timestamp'], reporter_id)
        
        cursor.execute(sql, values)
        db.commit()
        logger.info(f"Data saved to MySQL for reporter {reporter_id}")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

def main():
    my_id = 'dsy4qx'
    my_name = 'Julie Wang'
    register_reporter('reporters', my_id, my_name)
    for i in range(10):
        logger.info(f"Start looping {i + 1}/10 ---")
        raw_data = extract()
        if raw_data:
            transformed_df = transform(raw_data)
            load(transformed_df, my_id)
        if i < 9:
            logger.info("Waiting...")
            time.sleep(5)

if __name__ == "__main__":
    main()