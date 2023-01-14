Dev environment looks like this, which uses interactive (user) login for authentication to Azure ML for mlflow tracking URI

```
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication
import mlflow

subscription_id = 'c0ec2c2e-0f01-4055-8fe1-41b726d49380'
resource_group = 'msft-hudua-dev-rg'
workspace_name = 'msft-hudua-dev-aml'
interactive_auth = InteractiveLoginAuthentication(tenant_id="16b3c013-d300-468d-ac64-7eda0820b6d3")
ws = Workspace.get(name=workspace_name,
                   subscription_id=subscription_id,
                   resource_group=resource_group,
                   auth = interactive_auth
                  )
```

Prod environment looks like this, which uses a service principal for Azure ML authentication for mlflow tracking URI

```
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
import mlflow

subscription_id = 'c0ec2c2e-0f01-4055-8fe1-41b726d49380'
resource_group = 'msft-hudua-prod-rg'
workspace_name = 'msft-hudua-prod-aml'
secret = dbutils.secrets.get(scope = 'kv', key = 'dlmountsp')
sp = ServicePrincipalAuthentication(tenant_id="16b3c013-d300-468d-ac64-7eda0820b6d3",
                                    service_principal_id="1e14eba4-fcba-4795-bb2e-71eea073e6a6",
                                    service_principal_password=secret)
ws = Workspace.get(name=workspace_name,
                   subscription_id=subscription_id,
                   resource_group=resource_group,
                   auth=sp)
mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())
```
