import sys
from databricks_api import DatabricksAPI
import time, json

token = sys.argv[1]
build_id = sys.argv[2]
print(env)


host = 
repo_id = 
cluster_id = 

db = DatabricksAPI(
    host=host,
    token=token
)

db.repos.update_repo(
    id = repo_id,
    branch='main'
)

job_id = db.jobs.create_job(
    name="ml-ops-model-training-{}".format(build_id),
    existing_cluster_id=cluster_id,
    notebook_task={"notebook_path":"/Repos/EnterpriseMLHub/MLHub/Model/modeling"}
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
    elif status == 'FAILED':
        raise Exception('Job failed')
    else:
        print('Job is not successful yet, waiting 1 minute')
        time.sleep(60)
if i == N - 1:
    raise Exception('job timed out after 30 mins. Please check Databricks job')
