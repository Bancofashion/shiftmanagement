#!/bin/bash

# Server credentials
SERVER_IP="69.28.88.205"
USERNAME="root"
PASSWORD="kY2hkWFErBgPf3t5"

# Create SSH key if it doesn't exist
if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
fi

# Copy SSH key to server
sshpass -p "$PASSWORD" ssh-copy-id -o StrictHostKeyChecking=no "$USERNAME@$SERVER_IP"

# Install required packages on server
ssh "$USERNAME@$SERVER_IP" << EOF
    apt-get update
    apt-get install -y docker.io docker-compose git
    systemctl start docker
    systemctl enable docker
EOF

# Copy project files to server
scp -r . "$USERNAME@$SERVER_IP:/root/shift-service"

# Deploy application
ssh "$USERNAME@$SERVER_IP" << EOF
    cd /root/shift-service
    docker-compose down
    docker-compose build --no-cache
    docker-compose up -d
EOF

echo "Deployment completed! Your application is now running at http://69.28.88.205" 