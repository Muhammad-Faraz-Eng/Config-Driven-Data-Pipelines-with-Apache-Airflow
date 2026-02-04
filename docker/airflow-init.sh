# !/usr/bin/env bash
set -e

echo "⏳ Waiting for PostgreSQL..."
sleep 10

echo "🗄️ Initializing Airflow DB..."
airflow db init

echo "👤 Creating Airflow admin user..."
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

echo "✅ Airflow initialization complete"
