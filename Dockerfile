# Base image
FROM python:3.12.3

# Working directory set karo
WORKDIR /app

# Requirements copy aur install karo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki files copy karo
COPY . .

# FastAPI port
EXPOSE 8000

# App start karo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]