FROM python:3.11.2-alpine

WORKDIR /usr/src/app

RUN apk add build-base libpq-dev

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ./build.sh && gunicorn -b 0.0.0.0:8000 Blog.wsgi:application 