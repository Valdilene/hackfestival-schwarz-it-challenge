# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run migrations and start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
