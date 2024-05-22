This is the main repository of [remla24-team10](https://github.com/remla24-team10)
Operation: https://github.com/remla24-team10/operation/tree/main

Relevant versions have been tagged with tag "a2"


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

The README file contains the architecture, installations and comments for each assignments.

