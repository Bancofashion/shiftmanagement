FROM python:3.11

WORKDIR /app

# Update pip and install packages one by one
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir fastapi==0.88.0
RUN pip install --no-cache-dir uvicorn==0.20.0
RUN pip install --no-cache-dir sqlalchemy==1.4.23
RUN pip install --no-cache-dir pymysql
RUN pip install --no-cache-dir python-jose[cryptography]
RUN pip install --no-cache-dir passlib[bcrypt]
RUN pip install --no-cache-dir python-multipart
RUN pip install --no-cache-dir email-validator
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir apscheduler
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir reportlab
RUN pip install --no-cache-dir Pillow
RUN pip install --no-cache-dir python-dateutil

# Copy the rest of the application
COPY . .

# Make the wait script executable
RUN chmod +x wait_for_mysql.py

# Command to run the application
CMD ["sh", "-c", "python wait_for_mysql.py && uvicorn main:app --host 0.0.0.0 --port 8000"] 