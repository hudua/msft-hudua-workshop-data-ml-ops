# Databricks notebook source
# MAGIC %run ./mlflow-utils-env

# COMMAND ----------

import mlflow
import azureml.mlflow
import datetime
from azureml.core import Model

# COMMAND ----------

print('this is a live test at Saturday 12:19am')

# COMMAND ----------

import pandas as pd
df = pd.read_csv('/dbfs/mnt/raw/sample_data.csv')

# COMMAND ----------

df[['rpm','angle','temperature','humidity','windspeed','power']].corr()

# COMMAND ----------

model_dataset = df[['humidity','power']]
print("Here is the correlation...", model_dataset.corr())

# COMMAND ----------

model_dataset.plot.scatter(x = 'humidity',y='power')

# COMMAND ----------

train_test_split_ratio = 0.7

# COMMAND ----------

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

print("Now we train linear regression model based on train/test split")

eva_model = LinearRegression()
X = np.array(model_dataset['humidity']).reshape(-1, 1)
y = np.array(model_dataset['power']).reshape(-1, 1)

# COMMAND ----------

X_train, X_test, X_train, y_test = train_test_split(X, y, test_size = 1-train_test_split_ratio)


# COMMAND ----------

eva_model.fit(X_train, X_train)

# COMMAND ----------

y_pred = eva_model.predict(X_test)
abs_error = np.mean(np.abs(y_pred - y_test))

# COMMAND ----------

print("Here is the absolute error", abs_error)

# COMMAND ----------

print("Now we train model on the entire dataset")

model = LinearRegression()
model.fit(X,y)

# COMMAND ----------

experiment_name = 'mlops_end2end'
mlflow.set_experiment(experiment_name)

print("Now we use mlflow to track experiments")

with mlflow.start_run() as mlflow_run:
    mlflow.log_param("trainingdatetime", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    mlflow.log_metric("train_test_split", train_test_split_ratio)
    mlflow.log_metric("abs_error", abs_error)


# COMMAND ----------

import pickle, os

print("Now we use Azure ML to register model in AML registry")
pickle.dump(model, open('/tmp/model.pkl', 'wb'))
model = Model.register(workspace = ws,
                       model_name="mlopsmodel2",
                       model_path = "/tmp/model.pkl",
                       description = 'Regression Model 2'
                      )
