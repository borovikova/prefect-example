import pandas as pd
from prefect import flow, task

@task
def create_and_print_dataframe():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    print(df)

@flow
def pandas_flow():
    create_and_print_dataframe()

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/borovikova/prefect-example.git",
        entrypoint="my_workflow.py:pandas_flow",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",
        cron="0 1 * * *",
    )
