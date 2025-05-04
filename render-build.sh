#!/bin/bash
set -e # Exit on error

echo "Starting build script..."

# Update package lists
echo "Updating package lists..."
apt-get update

# Install unixODBC dependencies
echo "Installing unixODBC..."
apt-get install -y unixodbc-dev

# Add Microsoft repository for ODBC Driver
echo "Adding Microsoft repository..."
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update package lists again
echo "Updating package lists after adding Microsoft repo..."
apt-get update

# Install ODBC Driver 18
echo "Installing ODBC Driver 18 for SQL Server..."
ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Verify ODBC driver installation
echo "Verifying ODBC drivers..."
odbcinst -q -d

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r backend/requirements.txt

echo "Build script completed successfully!"