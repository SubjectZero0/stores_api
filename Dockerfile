FROM python:3.11.1-alpine3.16

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    adduser \
        --disabled-password \
        --no-create-home \
        flask-user && \
    mkdir -p /vol/web/static && \
    mkdir p /vol/web/media && \
    chown -R flask-user:flask-user /vol && \
    chmod -R 755 /vol

USER flask-user
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]