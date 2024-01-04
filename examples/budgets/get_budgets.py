from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

created = a.budgets.create(budget=billing.Budget(
    name=f'sdk-{time.time_ns()}',
    filter="tag.tagName = 'all'",
    period="1 month",
    start_date="2022-01-01",
    target_amount="100",
    alerts=[billing.BudgetAlert(email_notifications=["admin@example.com"], min_percentage=50)]))

by_id = a.budgets.get(budget_id=created.budget.budget_id)

# cleanup
a.budgets.delete(budget_id=created.budget.budget_id)
