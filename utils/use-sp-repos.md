In order to use a service principal's Databricks personal access token to update a repo. You will have to do the following.

First you need to run the Git Credentials API through your service principal to update your DevOps Repo personal access token

```
POST: https://adb-<id>.azuredatabricks.net/api/2.0/git-credentials
Authorization: Bearer <sp-token>
Body
{
  "personal_access_token": "",
  "git_username": "name@domain.com",
  "git_provider": "azureDevOpsServices"
}
```

Then you need to use this service principal to create the repo:

```
POST https://adb-<id>.azuredatabricks.net/api/2.0/repos
Authorization: Bearer <sp-token>
Body
{
  "url": "https://github.com/jsmith/test",
  "provider": "azureDevOpsServices",
  "path": "/Repos/Production/testrepo"
}
```

Then you can run repo update:
```
PATCH https://adb-<id>.azuredatabricks.net/api/2.0/repos/<repo-id>
Authorization: Bearer <sp-token>
Body
{
    "branch": "main"
}
```
