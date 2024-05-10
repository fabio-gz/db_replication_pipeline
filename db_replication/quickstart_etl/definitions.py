from dagster import Definitions, load_assets_from_modules
from .assets import Aw_replication
from .resources import sling_resources

sling_assets = load_assets_from_modules(modules=[Aw_replication])

defs = Definitions(
    assets=[*sling_assets],
    resources={
        'sling': sling_resources.sling
    }
)
