# Azure Machine Learning Workshop 1

## Introduction
This Azure Machine Learning (AML) workshop is based on the [DP100 MSLearn](https://github.com/MicrosoftLearning/mslearn-dp100) lab files. The lab has been tailored to introduce excerises for the learns that require them to referece MS Docs in order to complete TODO's. These TODO's are meant to focus on core componetns of the AML workspace and Python SDK. 

I addition, this workshop introduces exersices for data egineering pipelines in Azure Data Factory (ADF) that are used for training and scoring pipelines. Scoring, monitoring, and retraining ML models in production are core activities of [MLOps](https://en.wikipedia.org/wiki/MLOps). This workshop attempts to simplify this rather complex story by focusing on patterns that rely more heavly on Azure Data Factory for orchastration. The presence of DevOps CI/CD is currently ommitted from this workshop, with plans of introducing it in the future to support the relase of artificats between environemnts (i.e. dev, stage, prod).

By the end of this workshop learners will build two ADF pipelines that orchestrate a number of AML pipelines. The image below helps visualize the scoring and training pipelines that the AML pipelines steps that they will orchestrate.

The workshop will conclude with an example of the AML data drift feature and how it can be used to determine when the ADF training pipeline should run for retraining the ML model.

![ADF pipelines for training and scoring that call AML pipelines for each step of the process](code\img\readmearchitecture.png)

<!--
Prerequisites
-Service Principal (AML->ADLS)
-->

## Lab Modules
The workshop will consists of four modules that include a varying number of exersices. Completing the modules in order is design to build an understanding of the AML workspace. The following modules focus on building pipelines to train, deploy and score ML models. This is design to leave learners with an understanding of the basic pattern for operationalizing ML models with AML + ADF.

### Module 1: Getting started 
 
1. [Getting started with notebooks](../code/Get%20Started%20with%20Notebooks.ipynb)

1. [Running Experiments]()

1. [Work with Data]()

1. [Train & Register Models]()

### Module 2: Visual Designer Pipeline

1. [Visual Designer Data Prep Pipeline]()


### Module 3: Inferencing/Scoring

1. [Create Real-time Inferencing Service]()

1. [Batch Inference Pipeline]()

### Module 4: Retraining Pattern

1. [Connecting Azure Data Factory]()

1. [Data Factory Training Pipeline]() 

1. [Data Factory Scoring Pipeline]()

1. [Data Drift Monitor]()

