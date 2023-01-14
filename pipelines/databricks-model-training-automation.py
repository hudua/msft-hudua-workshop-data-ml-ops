import sys
from databricks_api import DatabricksAPI

token = sys.argv[1]

db = DatabricksAPI(
    host="https://adb-312205465995014.14.azuredatabricks.net/",
    token=token
)

db.repos.update_repo(
    id = 2580158515741092,
    branch='main'
)
