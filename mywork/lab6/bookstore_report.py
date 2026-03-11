import os
import pymongo
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGODB_ATLAS_URL")
MONGO_USER = os.getenv("MONGODB_ATLAS_USER")
MONGO_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
    connection_string = f"mongodb+srv://{MONGO_USER}:{MONGO_PWD}@{MONGO_URL.split('://')[1]}"
    
    try:
        client = MongoClient(connection_string)

        db = client["bookstore"]
        authors_col = db["authors"]
        
        print("-" * 30)
        print("BOOKSTORE AUTHOR REPORT")
        print("-" * 30)
        
        total_authors = authors_col.count_documents({})
        print(f"Total Authors in Database: {total_authors}")
        print("-" * 30)
        
        authors = authors_col.find({})
        for author in authors:
            name = author.get("name", "N/A")
            nationality = author.get("nationality", "N/A")
            birthday = author.get("birthday", "Unknown")
            
            print(f"Name: {name}")
            print(f"Nationality: {nationality}")
            print(f"Birthday: {birthday}")
            print("-" * 10)
            
        client.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()