Here is how to generate an Azure Databricks personal access token from using a service principal.

1. Get AAD access token for service principal (easiest way is to run AZ CLI) - keep the resource id the same (starting with 2ff8… the same as that is Databricks’ unique resource ID)

```
az login --service-principal -u <client-id> -p <secret> --tenant <tenant-id>
az account get-access-token --resource 2ff814a6-3304-4ab8-85cb-cd0e6f879c1d
```

2. Then with a user access token (of someone who has sufficient permission), give service principal workspace access

```
POST https://adb-<id>.azuredatabricks.net/api/2.0/preview/scim/v2/ServicePrincipals
Authorization: Bearer <user-personal-access-token>
Body

{
  "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:ServicePrincipal" ],
  "applicationId": "<clientid>",
  "displayName": "name",
  "groups": [
    {
      "value": "<group-id>"
    }
  ],
  "entitlements": [
    {
      "value":"allow-cluster-create"
    }
  ]
}

```

You will want to create a group to specify where the service principal should belong to by calling:

```
GET: 2.0/preview/scim/v2/Groups
```

3. Then, provide this service principal permission in Databricks workspace to be able to use PAT

4. Finally, use the service principal AAD token to generate a Personal Access Token:

```
POST https://adb-<id>.azuredatabricks.net/api/2.0/token/create
Authorication: Bearer <AAD token>
Body: { "comment": "This is an example token", "lifetime_seconds": 7776000 }
```
