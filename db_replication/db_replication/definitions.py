from dagster import Definitions, load_assets_from_modules
from .assets import Aw_replication, dbt
from .resources import sling_resources

sling_assets = load_assets_from_modules(modules=[Aw_replication])
dbt_assets = load_assets_from_modules(modules=[dbt])

defs = Definitions(
    assets=[*sling_assets, *dbt_assets],
    resources={
        'sling': sling_resources.sling,
        'dbt': sling_resources.dbt_resource
    }
)
