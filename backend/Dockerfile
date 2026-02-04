# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Production stage
FROM python:3.11-slim as production

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app.py .

# Make sure we use packages from .local
ENV PATH=/root/.local/bin:$PATH

# Expose port
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]

# Single-stage Dockerfile (alternative)
# FROM python:3.11-slim
# 
# WORKDIR /app
# 
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# 
# COPY app.py .
# 
# EXPOSE 5001
# 
# CMD ["python", "app.py"]