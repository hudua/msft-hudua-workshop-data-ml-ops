Here is how to generate an Azure Databricks personal access token from using a service principal.

1. Get AAD access token for service principal (easiest way is to run AZ CLI) - keep the resource id the same (starting with 2ff8… the same as that is Databricks’ unique resource ID)

```
az login --service-principal -u <client-id> -p <secret> --tenant <tenant-id>
az account get-access-token --resource 2ff814a6-3304-4ab8-85cb-cd0e6f879c1d
```
