FROM python:3.12-slim

WORKDIR /app

# Install Java + system tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jdk curl procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/default-java

# Install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application and dataset
COPY app.py sales.csv ./

CMD ["python", "app.py"]



#docker build -t assign17-spark .
#docker run --rm -v "$PWD/output:/app/output" assign17-spark