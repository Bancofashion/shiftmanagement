FROM python:3.11

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pymysql

# Copy the rest of the application
COPY . .

# Make the wait script executable
RUN chmod +x wait_for_mysql.py

# Create necessary directories
RUN mkdir -p uploaded_facturen uploads/loonstroken

# Command to run the application
CMD ["sh", "-c", "python wait_for_mysql.py && uvicorn main:app --host 0.0.0.0 --port 8000"] 