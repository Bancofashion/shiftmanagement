import time
import pymysql
import os

def wait_for_mysql():
    max_retries = 30
    retry_count = 0
    db_host = os.getenv("DB_HOST", "db")
    db_port = int(os.getenv("DB_PORT", "3306"))
    db_user = os.getenv("DB_USER", "planner_user")
    db_password = os.getenv("DB_PASSWORD", "q5nRgHumCV")
    db_name = os.getenv("DB_NAME", "planner_db")

    while retry_count < max_retries:
        try:
            conn = pymysql.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_name
            )
            conn.close()
            print("MySQL is ready!")
            return True
        except pymysql.Error as e:
            print(f"Waiting for MySQL... (attempt {retry_count + 1}/{max_retries})")
            retry_count += 1
            time.sleep(2)

    print("Failed to connect to MySQL after maximum retries")
    return False

if __name__ == "__main__":
    wait_for_mysql()
