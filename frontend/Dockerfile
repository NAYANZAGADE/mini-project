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
COPY . .

# Make sure we use packages from .local
ENV PATH=/root/.local/bin:$PATH

# Set environment variable for backend URL
ENV BACKEND_URL=http://backend:5001

# Expose port
EXPOSE 3000

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
# COPY . .
# 
# ENV BACKEND_URL=http://backend:5001
# 
# EXPOSE 3000
# 
# CMD ["python", "app.py"]