airflow-config-driven-pipelines/
│
├── docker/
│ ├── Dockerfile
│ ├── docker-compose.yml
│ └── airflow-init.sh
│
├── src/
│ ├── core/
│ │ ├── base/
│ │ │ ├── base_pipeline.py
│ │ │ ├── base_source.py
│ │ │ ├── base_target.py
│ │ │ ├── base_transformation.py
│ │ │ └── base_connector.py
│ │ │
│ │ ├── factories/
│ │ │ ├── source_factory.py
│ │ │ ├── target_factory.py
│ │ │ └── transformation_factory.py
│ │ │
│ │ ├── config/
│ │ │ ├── config_loader.py
│ │ │ ├── config_validator.py
│ │ │ ├── template_engine.py
│ │ │ └── connection_registry.py
│ │ │
│ │ ├── connectors/
│ │ │ └── postgres_connector.py
│ │ │
│ │ ├── sources/
│ │ │ └── postgres_source.py
│ │ │
│ │ ├── targets/
│ │ │ └── postgres_target.py
│ │ │
│ │ ├── transformations/
│ │ │ └── identity_transformation.py
│ │ │
│ │ └── dag/
│ │ └── dag_factory.py
│ │
│ ├── dags/
│ │ └── auto_generated/
│ │ └── pipeline_dag_loader.py
│ │
│ └── configs/
│ ├── pipelines/
│ │ └── postgres_to_postgres.yaml
│ └── templates/
│ └── pipeline_template.yaml
│
├── .env
└── README.md