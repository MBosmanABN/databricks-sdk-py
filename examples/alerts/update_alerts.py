from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

srcs = w.data_sources.list()

query = w.queries.create(name=f'sdk-{time.time_ns()}',
                         data_source_id=srcs[0].id,
                         description="test query from Go SDK",
                         query="SELECT 1")

alert = w.alerts.create(options=sql.AlertOptions(column="1", op="==", value="1"),
                        name=f'sdk-{time.time_ns()}',
                        query_id=query.id)

w.alerts.update(options=sql.AlertOptions(column="1", op="==", value="1"),
                alert_id=alert.id,
                name=f'sdk-{time.time_ns()}',
                query_id=query.id)

# cleanup
w.queries.delete(query_id=query.id)
w.alerts.delete(alert_id=alert.id)
