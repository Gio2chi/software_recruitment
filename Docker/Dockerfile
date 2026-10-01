FROM python:3.12-slim

WORKDIR /app
COPY index.html /app/

EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]