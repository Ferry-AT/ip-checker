FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system deps (curl for healthchecks, useful debugging)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python deps (including requests[socks])
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY ip_checker.py .

# Run script
CMD ["python", "ip_checker.py"]
