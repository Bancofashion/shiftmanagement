FROM python:3.11

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Copy requirements file
COPY requirements.txt .

# Install dependencies one by one
RUN pip install --no-cache-dir fastapi==0.88.0
RUN pip install --no-cache-dir uvicorn==0.20.0
RUN pip install --no-cache-dir sqlalchemy==1.4.23
RUN pip install --no-cache-dir pymysql
RUN pip install --no-cache-dir python-jose[cryptography]==3.3.0
RUN pip install --no-cache-dir passlib[bcrypt]==1.7.4
RUN pip install --no-cache-dir python-multipart==0.0.5
RUN pip install --no-cache-dir python-dotenv==0.19.0
RUN pip install --no-cache-dir email-validator==1.1.3
RUN pip install --no-cache-dir requests==2.26.0
RUN pip install --no-cache-dir aiofiles==0.7.0
RUN pip install --no-cache-dir python-dateutil==2.8.2

# Copy the rest of the application
COPY . .

# Make the wait script executable
RUN chmod +x wait_for_mysql.py

# Create necessary directories
RUN mkdir -p uploaded_facturen uploads/loonstroken

# Command to run the application
CMD ["sh", "-c", "python wait_for_mysql.py && uvicorn main:app --host 0.0.0.0 --port 8000"] 