FROM python:3.11

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymysql

# Copy the rest of the application
COPY . .

# Make the wait script executable
RUN chmod +x wait_for_mysql.py

# Command to run the application
CMD ["sh", "-c", "python wait_for_mysql.py && uvicorn main:app --host 0.0.0.0 --port 8000"] 