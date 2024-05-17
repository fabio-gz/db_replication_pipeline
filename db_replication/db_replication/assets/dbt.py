from pathlib import Path
from dagster import AssetExecutionContext, AssetKey
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator
import os
from ..resources import sling_resources
from .constants import DBT_DIRECTORY


class CustomizedDagsterDbtTranslator(DagsterDbtTranslator):
    def get_asset_key(self, dbt_resource_props):
        resource_type = dbt_resource_props["resource_type"]
        name = dbt_resource_props["name"]
        if resource_type == "source":
            return AssetKey(name)
        else:
            return super().get_asset_key(dbt_resource_props)

dbt_manifest_path = os.path.join(DBT_DIRECTORY, "target", "manifest.json")


@dbt_assets(manifest=dbt_manifest_path, dagster_dbt_translator=CustomizedDagsterDbtTranslator())
def dbt_transformations(context: AssetExecutionContext, dbt:DbtCliResource):
    yield from dbt.cli(['run'], context=context).stream()