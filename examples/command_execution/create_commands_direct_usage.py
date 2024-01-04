from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]

context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()

# cleanup
w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)
