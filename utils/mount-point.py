# Databricks notebook source
secret = dbutils.secrets.get(scope = 'kv', key = 'dlmountsp')
configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": "9980d64f-f2a1-4711-9a58-e5fa65ceff0a",
       "fs.azure.account.oauth2.client.secret": secret,
       "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/16b3c013-d300-468d-ac64-7eda0820b6d3/oauth2/token",
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}

dbutils.fs.mount(
source = "abfss://raw@msfthuduadevdl.dfs.core.windows.net",
mount_point = "/mnt/raw",
extra_configs = configs)
