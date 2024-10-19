# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
# Copy templates/
COPY templates/ /app/templates/

# Copy trained_model/
COPY trained_model/ /app/trained_model/

# Copy requirements.txt
COPY requirements.txt /app

# Copy app.py
COPY app.py /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
