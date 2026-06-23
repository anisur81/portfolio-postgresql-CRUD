# Use the official Python image
#FROM python:3.12.3
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /portfolio

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/portfolio

# Copy the entire project into the container
COPY . /portfolio


RUN apt-get update && apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install gunicorn django whitenoise

RUN python manage.py collectstatic --noinput

# Expose port 8000 for the Django development server final
EXPOSE 8000

# Default command to run the Django server

CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "5"]
