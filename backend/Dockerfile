FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gnupg2 \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9 6ED0E7B82643E131 F8D2585B8783D481 54404762BBB6E853 BDE6D2B9216EC7A8 \
    && apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

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