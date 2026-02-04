# Airflow Config‑Driven Pipelines

A **configuration‑driven data pipeline framework** built on **Apache Airflow** where pipelines are defined using **YAML** and **auto‑registered as DAGs**.

This project implements a **Postgres → Postgres** pipeline using **pure Python libraries** (psycopg2, SQLAlchemy, pandas) and **does not use Airflow hooks**.

---

## Objectives

- Define pipelines declaratively using YAML
- Auto‑generate Airflow DAGs from configuration
- Separate orchestration (Airflow) from execution logic
- Support pluggable sources, targets, and transformations
- Centralize connection management
- Keep DAG files minimal and generic

## High‑Level Flow
```text
Pipeline YAML
  → Config Loader
  → Config Validator
  → DAG Factory
  → BasePipeline
       ├─ Source
       ├─ Transformations
       └─ Target
```

## Project Structure

See detailed layout in [project_structure.md](file:///d:/Data%20Engineering/Practice/Projects/airflow-config-driven-pipelines/docs/project_structure.md)


---

## Pipeline Configuration

**File:** `src/configs/pipelines/postgres_to_postgres.yaml`

```yaml
pipeline:
  name: postgres_to_postgres_users
  description: Copy users table from source Postgres to target Postgres
  schedule: "@daily"
  start_date: "2024-01-01"
  catchup: false
  retries: 1

  source:
    type: postgres
    connection_id: src_postgres
    schema: public
    table: users

  transformations:
    - type: identity
      params: {}

  target:
    type: postgres
    connection_id: tgt_postgres
    schema: analytics
    table: users
    write_mode: overwrite

Pipeline Template
File: src/configs/templates/pipeline_template.yaml
pipeline:
  name: string
  description: string
  schedule: string
  start_date: string
  catchup: boolean
  retries: integer

  source:
    type: string
    connection_id: string
    schema: string
    table: string

  transformations:
    - type: string
      params: dict

  target:
    type: string
    connection_id: string
    schema: string
    table: string
    write_mode: string

Connection Management
Connections are resolved from environment variables via ConnectionRegistry and referenced by connection_id.

For connection_id X, required env vars:
- X uppercased + _HOST, _PORT, _DB, _USER, _PASSWORD

Example (.env):
```env
# Airflow
AIRFLOW_UID=50000
AIRFLOW_GID=0

# Source Postgres (src_postgres)
SRC_POSTGRES_HOST=postgres
SRC_POSTGRES_PORT=5432
SRC_POSTGRES_DB=airflow
SRC_POSTGRES_USER=airflow
SRC_POSTGRES_PASSWORD=airflow

# Target Postgres (tgt_postgres)
TGT_POSTGRES_HOST=postgres
TGT_POSTGRES_PORT=5432
TGT_POSTGRES_DB=airflow
TGT_POSTGRES_USER=airflow
TGT_POSTGRES_PASSWORD=airflow
```

This keeps credentials centralized, pipelines portable, configs environment‑agnostic

DAG Auto‑Generation
File: pipeline_dag_loader.py

Responsibilities:

Scan configs/pipelines/

Load all YAML pipeline definitions

Validate schema

Create DAGs using dag_factory.py

Register DAGs dynamically using globals()

Every valid pipeline YAML becomes an Airflow DAG automatically.

Core Components
BasePipeline
Orchestrates pipeline execution

Calls:

source.connect()

source.read()

transformations

target.write()

cleanup

Sources
Responsible for reading data

Return pandas DataFrames

Example: PostgresSource

Transformations
Stateless DataFrame operations

Executed sequentially

Example: IdentityTransformation

Targets
Persist DataFrames

Handle write modes

Example: PostgresTarget

Connectors
Pure Python DB connectivity

psycopg2 + SQLAlchemy

No Airflow hooks used

Running the Project
1. Create .env (see example above)
2. Start Airflow:
```bash
docker-compose up -d
```
3. Open the Airflow UI: http://localhost:8080
4. Trigger the pipeline DAG (ID from pipeline.name), e.g.:
```text
postgres_to_postgres_users
```
Trigger manually from the Airflow UI.

Testing
Insert data into the source Postgres table

Trigger the DAG

Verify data in the target table

Inspect Airflow task logs

Design Decisions
No Airflow Hooks

No per‑pipeline DAG files

No credentials in pipeline configs

Airflow used only for orchestration

Current Status
DAG auto‑registration working

Postgres → Postgres pipeline functional

End‑to‑end execution verified

Design Philosophy
Configuration defines behavior
Framework executes logic
Airflow orchestrates
