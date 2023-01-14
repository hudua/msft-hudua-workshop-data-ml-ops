import sys
from databricks_api import DatabricksAPI
import time

tokenuser = sys.argv[1]
build_id = sys.argv[2]

db = DatabricksAPI(
    host="https://adb-312205465995014.14.azuredatabricks.net/",
    token=tokenuser
)

db.repos.update_repo(
    id = 2580158515741092,
    branch='main'
)

job_id = db.jobs.create_job(
    name="ml-ops-model-training-{}".format(build_id),
    existing_cluster_id="0114-031312-mfx6svv5",
    notebook_task={"notebook_path":"/Repos/msft-hudua-data-ml-ops/repo/ml/main"}
)['job_id']

run_id = db.jobs.run_now(
    job_id=job_id
)['run_id']

N = 30
for i in range(N):
    try:
        status = db.jobs.get_run(run_id=run_id)['state']['result_state']
    except:
        status = 'UNKNOWN'
    if status == 'SUCCESS':
        print('Job is successful')
        break
    else:
        print('Job is not successful yet, waiting 1 minute')
        time.sleep(60)
if i == N - 1:
    raise Exception('job timed out after 30 mins. Please check Databricks job')
        
