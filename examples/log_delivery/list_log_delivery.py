from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

all = a.log_delivery.list(billing.ListLogDeliveryRequest())
