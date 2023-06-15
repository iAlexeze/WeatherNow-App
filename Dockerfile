# Use the official Python base image
FROM python:slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set environment variables
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
ENV WEATHERAPI_API_KEY=6df85af860034db4863201713231406
ENV OPENAI_API_KEY=sk-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


# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD [ "python", "main.py" ]
