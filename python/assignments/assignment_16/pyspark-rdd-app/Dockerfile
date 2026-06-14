FROM python:3.12-slim

WORKDIR /app

# Install system dependencies and Java (required for Apache Spark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jdk procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Environment Variables for Java
ENV JAVA_HOME=/usr/lib/jvm/default-java

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the dataset into the container
COPY employees.csv .

# Expose the default JupyterLab port
EXPOSE 8888

# Start JupyterLab when the container runs
# --ip=0.0.0.0 allows connections from outside the container
# --allow-root is necessary because Docker containers run as root by default
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]