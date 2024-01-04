from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

public_share_recipient = """{
        "shareCredentialsVersion":1,
        "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
        "endpoint":"https://sharing.delta.io/delta-sharing/"
    }
"""

created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)

_ = w.providers.update(name=created.name, comment="Comment for update")

# cleanup
w.providers.delete(name=created.name)
