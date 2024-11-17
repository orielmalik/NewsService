# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# התקנת הדרישות
COPY requirements.txt .
RUN pip install -r requirements.txt

# העתקת קבצי האפליקציה
COPY . .

# הפעלת האפליקציה
CMD ["python", "app.py"]
