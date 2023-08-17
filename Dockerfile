# Base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project
COPY . .

# Set environment variables
ENV BOT_TOKEN=${BOT_TOKEN}
ENV DEBUG=${DEBUG}
ENV SECRET_KEY=${SECRET_KEY}


# Install Gunicorn
RUN pip install gunicorn
EXPOSE 8000

# Run migrations and start Gunicorn
CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn notifier.wsgi:application --bind 0.0.0.0:8000