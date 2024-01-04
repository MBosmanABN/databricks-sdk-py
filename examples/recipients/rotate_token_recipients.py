from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.recipients.create(name=f'sdk-{time.time_ns()}')

recipient_info = w.recipients.rotate_token(name=created.name, existing_token_expire_in_seconds=0)

# cleanup
w.recipients.delete(name=created.name)
