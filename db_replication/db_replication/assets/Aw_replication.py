from dagster_embedded_elt.sling import SlingResource, sling_assets

from ..resources.sling_resources import replication_config




@sling_assets(replication_config=replication_config)
def replication_asset(context, sling: SlingResource):
    yield from sling.replicate(context=context)
    for row in sling.stream_raw_logs():
        context.log.info(row)