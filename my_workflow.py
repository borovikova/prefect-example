from prefect import flow

from constants import FLOW_NAME


@flow(name=FLOW_NAME)
def pandas_flow():
    ...
