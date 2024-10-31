# Start with the base image
FROM svizor/zoomcamp-model:3.11.5-slim

# Set the working directory
#WORKDIR /app

#COPY Pipfile Pipfile.lock /app/
COPY model1.bin dv.bin ./

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install Pipenv
RUN pip install pipenv

# Install all dependencies from the Pipfile
RUN pipenv install --deploy --ignore-pipfile --verbose

# Copy your Flask script
COPY q4.py ./ 

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app using Gunicorn
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "q4:app"]

# Build the Docker image
# docker build -t my-zoomcamp-model:latest .
#
# Run the Docker container
# docker run -p 8000:8000 my-zoomcamp-model:latest
