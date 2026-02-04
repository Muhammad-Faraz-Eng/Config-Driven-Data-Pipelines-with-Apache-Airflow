FROM apache/airflow:2.8.1-python3.10

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir \
    psycopg2-binary \
    pyyaml

ENV PYTHONPATH='/opt/airflow/src:${PYTHONPATH}'