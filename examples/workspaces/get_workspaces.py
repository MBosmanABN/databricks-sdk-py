from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

storage = a.storage.create(
    storage_configuration_name=f'sdk-{time.time_ns()}',
    root_bucket_info=provisioning.RootBucketInfo(bucket_name=os.environ["TEST_ROOT_BUCKET"]))

role = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))

created = a.workspaces.create(workspace_name=f'sdk-{time.time_ns()}',
                              aws_region=os.environ["AWS_REGION"],
                              credentials_id=role.credentials_id,
                              storage_configuration_id=storage.storage_configuration_id).result()

by_id = a.workspaces.get(workspace_id=created.workspace_id)

# cleanup
a.storage.delete(storage_configuration_id=storage.storage_configuration_id)
a.credentials.delete(credentials_id=role.credentials_id)
a.workspaces.delete(workspace_id=created.workspace_id)
