FROM python:3.8-slim-buster

# Install AWS CLI
RUN apt update -y && apt install awscli -y

# Set the working directory
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Display the contents of requirements.txt for debugging
RUN echo "Contents of requirements.txt:"
RUN cat requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]
