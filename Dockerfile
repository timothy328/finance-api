FROM python:3.9-slim  # Base image with Python 3.9

WORKDIR /app  # Set working directory

COPY requirements.txt requirements.txt  # Copy requirements file
RUN pip install -r requirements.txt  # Install dependencies

COPY . .  # Copy your entire project code

CMD ["python", "app.py"]  # Start command to run your application
