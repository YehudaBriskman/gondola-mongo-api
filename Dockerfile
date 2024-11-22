FROM python:3.11-bookworm

WORKDIR /app

RUN pip config set http.sslverify false

RUN pip config set global.no-cache-dir true

COPY . .

RUN pip install --no-cache-dir -r requirements.txt --disable-pip-version-check

EXPOSE 5002

CMD ["python", "app.py"]