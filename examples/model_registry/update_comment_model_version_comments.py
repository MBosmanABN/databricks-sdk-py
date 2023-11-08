from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

mv = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")

created = w.model_registry.create_comment(comment=f'sdk-{time.time_ns()}',
                                          name=mv.model_version.name,
                                          version=mv.model_version.version)

_ = w.model_registry.update_comment(comment=f'sdk-{time.time_ns()}', id=created.comment.id)

# cleanup
w.model_registry.delete_comment(id=created.comment.id)
