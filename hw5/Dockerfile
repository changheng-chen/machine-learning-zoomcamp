# Start with the base image
FROM svizor/zoomcamp-model:3.11.5-slim

# Set the working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/
COPY model1.bin dv.bin /app/

# Install Pipenv
RUN pip install pipenv

# Install all dependencies from the Pipfile
RUN pipenv install --deploy --ignore-pipfile --verbose

# Copy your Flask script
COPY q4.py /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app using Gunicorn
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "q4:app"]
