from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/borovikova/prefect-example.git",
        entrypoint="my_workflow.py:pandas_flow",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",
        cron="0 1 * * *",
    )
