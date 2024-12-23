from pendulum import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)

with DAG(
    dag_id="example_kubernetes_pod",
    schedule="@once",
    start_date=datetime(2023, 3, 30),
) as dag:
    example_kpo = KubernetesPodOperator(
        namespace="datamesh-demo",
        image="hello-world",
        name="airflow-test-pod",
        task_id="task-one",
        in_cluster=True,
        is_delete_operator_pod=True,
        get_logs=True,
        log_events_on_failure=True,
        env_vars={"NAME_TO_GREET": "Jey"},
    )

    example_kpo

