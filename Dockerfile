FROM python:3.8.6
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
RUN python manage.py collectstatic --noinput
CMD gunicorn ekroybikroy.wsgi:application --bind 0.0.0.0:8000