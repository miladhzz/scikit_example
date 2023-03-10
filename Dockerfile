# Use the official Python 3.10.9 image
FROM python:3.10.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=scikit.settings
ENV DB_PATH=/data/db.sqlite3

# Install project dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project code into the container
WORKDIR /code
COPY . /code/

# Create the SQLite database at the specified path
RUN mkdir -p /data && touch $DB_PATH && chmod 777 $DB_PATH

# Run migrations and start the server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
