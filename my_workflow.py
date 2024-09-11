import pandas as pd
from prefect import flow, task

from constants import FLOW_NAME


@task
def create_and_print_dataframe():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    print(df)

@flow(name=FLOW_NAME) # this causes an error during deployment
# @flow(name='test') # this works
def pandas_flow():
    create_and_print_dataframe()
