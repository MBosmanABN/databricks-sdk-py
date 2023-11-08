from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

public_share_recipient = """{
        "shareCredentialsVersion":1,
        "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
        "endpoint":"https://sharing.delta.io/delta-sharing/"
    }
"""

created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)

_ = w.providers.get(name=created.name)

# cleanup
w.providers.delete(name=created.name)
