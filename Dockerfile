# Use slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (cache optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

# Expose port
EXPOSE 5000

# Run as non-root user (best practice)
RUN useradd -m appuser
USER appuser

# Start app
CMD ["python", "app.py"]
