FROM python:3.11.3-slim
LABEL authors="bluetip"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update && apt install -y python3-dev && ln -s /usr/bin/python3 /usr/bin/python && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY bot ./

EXPOSE 80 88 443 8443

CMD ["python3", "-m", "main"]
