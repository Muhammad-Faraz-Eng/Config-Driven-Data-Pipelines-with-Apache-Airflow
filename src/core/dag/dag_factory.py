from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from core.base.base_pipeline import BasePipeline
from core.factories.source_factory import SourceFactory
from core.factories.target_factory import TargetFactory
from core.factories.transformation_factory import TransformationFactory


def create_dag(pipeline_config: dict):
    pipeline_cfg = pipeline_config["pipeline"]
    dag_id = pipeline_cfg["name"]

    default_args = {"retries": pipeline_cfg["retries"]}

    dag = DAG(
        dag_id=dag_id,
        description=pipeline_cfg["description"],
        schedule_interval=pipeline_cfg["schedule"],
        start_date=datetime.fromisoformat(pipeline_cfg["start_date"]),
        catchup=pipeline_cfg["catchup"],
        default_args=default_args,
    )
    with dag:

        def run_pipeline():
            source = SourceFactory.create(
                pipeline_cfg["source"]["type"], pipeline_cfg["source"]
            )

            transformations = [
                TransformationFactory.create(t["type"], t.get("params", {}))
                for t in pipeline_cfg["transformations"]
            ]

            target = TargetFactory.create(
                pipeline_cfg["target"]["type"], pipeline_cfg["target"]
            )

            pipeline_obj = BasePipeline(
                source=source, transformations=transformations, target=target
            )

            pipeline_obj.run()

        PythonOperator(task_id="run_pipeline", python_callable=run_pipeline)
    globals()[dag_id] = dag
    return dag
