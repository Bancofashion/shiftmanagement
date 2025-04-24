#!/bin/bash

echo "Waiting for MySQL to be ready..."
python wait_for_mysql.py

# Give MySQL a little extra time to fully initialize
sleep 5

# Fix database indexes
echo "Fixing database indexes..."
python fix_index.py

# Start the application
echo "Starting the application..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
