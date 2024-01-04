from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')

w.experiments.update_experiment(new_name=f'sdk-{time.time_ns()}', experiment_id=experiment.experiment_id)

# cleanup
w.experiments.delete_experiment(experiment_id=experiment.experiment_id)
