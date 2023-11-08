from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

smallest = w.clusters.select_node_type(local_disk=True)

created = w.instance_pools.create(instance_pool_name=f'sdk-{time.time_ns()}', node_type_id=smallest)

w.instance_pools.edit(instance_pool_id=created.instance_pool_id,
                      instance_pool_name=f'sdk-{time.time_ns()}',
                      node_type_id=smallest)

# cleanup
w.instance_pools.delete(instance_pool_id=created.instance_pool_id)
