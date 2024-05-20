# Operation

This is the main repository of [remla24-team10](https://github.com/remla24-team10)
The README file contains the architecture, installations and comments for each assignments.

## Architecture
- [app](https://github.com/remla24-team10/app) is the application that communicates with model-service and depends on lib-version 
- [lib-version](https://github.com/remla24-team10/lib-version) is version-aware library that can can be asked for the version of the library
- [model-service](https://github.com/remla24-team10/model-service) is a wrapper service for the released ML mod and is dependent on lib-ml
- [lib-ml](https://github.com/remla24-team10/lib-ml) contains the pre-processing logic for data that is used for training or queries
- [model-training](https://github.com/remla24-team10/model-training) contains the ML training pipeline and is dependent on lib-ml


## Installation

In this repository run the following commands:

```
git clone https://github.com/remla24-team10/model-service.git
```

```
git clone https://github.com/remla24-team10/app.git
```
```
docker-compose build
```


```
docker-compose up -d
```

You can then access the wep app via: [localhost](http://localhost:5000/) (if there is some issues try to open it in incognito)

[//]: # (# This README should introduce your highlevel architecture and that links to the corresponding repositories, so visitors can easily understand your project and find all relevant information. )


## Comments for A1
### Task 1: Organise your training pipeline following machine learning project best practices.
Pull request: https://github.com/janvandermeulen/REMLA-group10/pull/1 and https://github.com/janvandermeulen/REMLA-group10/pull/2 
Contributors: Shayan Ramezani and Jan van der Meulen
Reviewers: Jan van der Meulen,  Shayan Ramezani, Michael Chan, and Remi Lejeune. 

We chose poetry to handle all the packages. Instructions to set-up the project are added in the README. The codebase was written such that DVC can do a step-by-ste- reproduction. 

### Task 2: Enable collaborative development through a pipeline management tool (DVC)
Pull request: https://github.com/janvandermeulen/REMLA-group10/pull/4  
Contributor: Remi Lejeune
Reviewer: Michael Chan

We uploaded the data to the a remote gdrive cloud bucket using dvc. The data is now versioned and can be accessed by all team members.
Furthermore, we created a reproduction pipeline. We have encountered some issues with DVC pull and it may not pull from cloud, in which case run dvc repro to reproduce the files.

### Task 3: Report metrics using DVC
Pull request: https://github.com/janvandermeulen/REMLA-group10/pull/4  
See description of previous task. 

### Task 4: Audit code quality
Pull request: https://github.com/janvandermeulen/REMLA-group10/pull/3
Contributor: Michael Chan
Reviewer: Jan van der Meulen, Remi Lejeune and Shayan Ramezani

We used pylint and bandit to audit the code quality. The README provides instructions on how to run these tools. We fixed all the errors that the tools showed. Explanation for some of the configuration settings for both pylint and bandit:

A regex was created to accept names with a single capital letter between "_" as those are common names for matrix variables in data science, example of accepted names by regex: X_train, raw_X_train and X.
TODO warnings have been suppressed temporarily. As this is still the first version there are still many things that could be improved that have been
tagged as TODO for now, this should not affect the code quality.
The number of arguments and local variables allowed has been increased as it is common in data science to separate data such as train and test in separate local variables, this results in relatively more variables used.
Bandit warning B106 about potential hardcoded access tokens has been suppressed as it falsely triggers on the usage of the word token which is prevalent in data science projects and has nothing to do with password/auth tokens.

## Comments for A2 

### Task 1: App
Pull requests: https://github.com/remla24-team10/app/pull/1 and https://github.com/remla24-team10/app/pull/2 
Contributor: Jan van der Meulen
Reviewer: Remi Lejeune
We used Flask to create a simple web-app which imports the version-library and prompts the model-service for the result of a prediction. 

### Task 2: Lib-version
Pull requests: https://github.com/remla24-team10/lib-version/pull/1
Contributor: Jan van der Meulen
Reviewer: Shayan Ramezani
This is a automatically versioned library that can be asked for its own library. It updates the version number by automatically pulling the value from its own git tag. 

### Task 3: Model-service
Pull requests: https://github.com/remla24-team10/model-service/pull/1
Contributor: Michael Chan
Reviewer: Remi Lejeune
We used Flask to serve the model, the model itself is stored on gdrive and its downloaded at runtime.

### Task 4: Lib-ML 
Pull requests: https://github.com/remla24-team10/lib-ml/pull/7 and https://github.com/remla24-team10/lib-ml/pull/9
Contributor: Shayan Ramezani, Michael Chan
Reviewer: Michael Chan, Shayan Ramezani
This library provides several functions related to the processing of data. It is published on Pypi and has a workflow setup with github actions.

### Task 5: Model-training
Pull requests: https://github.com/remla24-team10/model-training/pull/2
Contributor: Shayan Ramezani 
Reviewer: Jan van der Meulen
Model training trains the model and stores all related files to drive via DVC. It was refactored in A2.

### Task 6: Operation
Pull request: https://github.com/remla24-team10/operation/pull/1
Contributor: Remi Lejeune
Reviewer: Jan van der Meulen

A docker compose file was created, which allow the app to be run easily. It creates two docker containers that communicate between eachother, a few other features were implemented namely: volume mapping, a port mapping, and
an environment variable.


## Comments for A3 

### Task 1: Setting up Virtual Infrastructure
Pull request: https://github.com/remla24-team10/operation/pull/3
Contributor: Jan van der Meulen
Reviewer: 

- We used Vagrant to create multiple virtual machines that run the app. After running ```vagrant up``` these can be accessed with the command ```vagrant ssh controller1```, ```vagrant ssh worker1``` and ```vagrant ssh worker2``` respectively.
- TODO: A non-trivial ansible script was created to install all the necessary software on the virtual machines.
- TODO: Each VM has a private network and can communicate directly with all other VMs. This can be tested by: 
- The Vagrantfile uses a loop and template arithmetics to create the VMs. As seen in the definition of the workers which can easily be scaled up to spawn as many workers as necessary. 
### Task 2: Setting up Software Environment
Pull request: 
Contributor: Shayan Ramezani and Remi Lejeune
Reviewer:

### Task 3: App Monitoring
Pull request:
Contributor: Michael Chan
Reviewer: 

### Task 4: Grafana 
Pull request: 
Contributor: Michael Chan
Reviewer:

