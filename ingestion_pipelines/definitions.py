from dagster import asset, Definitions

@asset
def hello_asset():
    return "Hello from Dagster!"

defs = Definitions(assets=[hello_asset])
