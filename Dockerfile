FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /find_me
COPY requirements.txt /find_me/
RUN pip install -r requirements.txt
COPY . /find_me/
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]