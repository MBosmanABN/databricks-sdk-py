from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

all = w.policy_families.list(compute.ListPolicyFamiliesRequest())

first_family = w.policy_families.get(policy_family_id=all[0].policy_family_id)
