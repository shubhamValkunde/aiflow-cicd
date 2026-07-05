FROM python:3.12-slim

WORKDIR /app

# Prevent Python bytecode + improve logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-root user (SECURITY)
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

# Install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Set ownership
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

EXPOSE 8000

# Production-friendly startup
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]