from pathlib import Path

from core.config.config_loader import ConfigLoader
from core.config.config_validator import ConfigValidator
from core.dag.dag_factory import create_dag

PROJECT_ROOT = Path("/opt/airflow/src")
PIPELINE_CONFIG_DIR = PROJECT_ROOT / "configs" / "pipelines"


def load_pipeline_dags() -> None:
    if not PIPELINE_CONFIG_DIR.exists():
        raise FileNotFoundError(
            f"pipeine config directory not found: {PIPELINE_CONFIG_DIR}"
        )

    for config_file in PIPELINE_CONFIG_DIR.glob("*.yaml"):
        loader = ConfigLoader("/opt/airflow/configs/pipelines")
        config = loader.load(config_file)

        ConfigValidator.validate(config)

        dag = create_dag(config)

        globals()[dag.dag_id] = dag


load_pipeline_dags()
