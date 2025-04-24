import time
import socket
import os

host = os.getenv("DB_HOST", "db")
port = 3306

print(f"Trying to connect to MySQL at {host}:{port}...")

for attempt in range(30):
    try:
        with socket.create_connection((host, port), timeout=2):
            print("✅ MySQL is ready!")
            break
    except OSError:
        print(f"⏳ Attempt {attempt + 1}: MySQL not ready yet...")
        time.sleep(2)
else:
    print("❌ Failed to connect to MySQL after 30 attempts.")
    exit(1)
