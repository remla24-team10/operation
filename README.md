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

The project can be ran using either docker compose or kubernetes (minikube). Vagrant currently creates VM's with some basic ansible playbooks but it currently is not functional yet.

### With Vagrant
Th VM's can be set up by running:
```
vagrant up
```
To access the machines use the following commands:
```
vagrant ssh controller
vagrant ssh worker1 
vagrant ssh worker2
```

### With docker compose
Run docker-compose:
```
docker compose up
```
The front-end application should now be available at localhost:5000.
### With kubernetes (minikube)
To run the project using minikube run the following commands:
Run:
```
minikube start
kubectl label ns operation istio-injection=enabled
kubectl apply -f operation-manifests.yaml
minikube tunnel
```
The project should now be available at localhost (no port) through ingress. 
Please wait a bit before making a request to the server, the server downloads the model on deployment which takes a few seconds.

### prometheus (Istio)
The project supports dashboards for various metrics utilising prometheus, for this to work the project has to be first ran using minikube.
```
istioctl dashboard prometheus
```

### prometheus (OLD)
The project supports dashboards for various metrics utilising prometheus, for this to work the project has to be first ran using minikube.
Additionally the prometheus stack should be installed through helm:
```
helm repo add myprom https://prometheus-community.github.io/helm-charts
helm install myprom prom-repo/kube-prometheus-stack
```
After reapplying operation-manifests.yaml the prometheus dashboard can be ran using:
```
minikube service myprom-kube-prometheus-sta-prometheus --url
```

### grafana
Grafana can also be used for further visualisation of the metrics, to run grafana prometheus should be active.
Run:
```
minikube service myprom-grafana --url
```
Afterwards login to the dashboard using the default credentials:
```
admin
prom-operator
```
The dashboard can now be imported by navigating to dashboards and importing the grafana.json file provided in the repository.


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
Reviewer: Shayan Ramezani

- We used Vagrant to create multiple virtual machines that run the app. After running ```vagrant up``` these can be accessed with the command ```vagrant ssh controller1```, ```vagrant ssh worker1``` and ```vagrant ssh worker2``` respectively.
- A non-trivial ansible script was created to install all the necessary software on the virtual machines. This can be found in ```ansible/playbook-controller.yml``` and ```ansible/playbook-worker.yml```.
- Each VM has a private network and can communicate directly with all other VMs. This can be tested by first ssh-ing into any of the machines. Then running pining another machine. E.g. 
  - ```vagrant ssh controller1```
  - ```ping 192.168.57.11``` to ping worker1.
- The Vagrantfile uses a loop and template arithmetics to create the VMs. As seen in the definition of the workers which can easily be scaled up to spawn as many workers as necessary. This is done by using the Python file: generate_inventory.py which generates the inventory for Ansible based on the amount of workers defined in the Vagrantfile. And, some simple looping in the Vagrantfile to create the workers.

### Task 2: Setting up Software Environment (ansible)
Pull request: https://github.com/remla24-team10/operation/pull/4
Contributor: Shayan Ramezani
Reviewer: Jan van der Meulen
- Currently still work in progress, there are still some problems creating the ansible playbooks to setup minikube.

### Task 3: Setting up Software Environment (minikube)
Pull request: https://github.com/remla24-team10/operation/pull/5
Contributor: Remi Lejeune
Reviewer: Michael Chan
- Now the app can be run using minikube and kubernetes. For both the front and backend `operation-manifests.yaml` contains a deployment, a service and ingress. Minikube utilises an ingress for the app to which has to be tunneled.

### Task 4: App Monitoring & Grafana
Pull request: https://github.com/remla24-team10/app/pull/3 & https://github.com/remla24-team10/operation/pull/6
Contributor: Michael Chan
Reviewer: Remi Lejeune
- Prometheus ServiceMonitor was used to collect metrics, which includes 2 gauges and a counter. A grafana json file was included in the repository which can be imported in grafana, it contains a dashboard with 3 panels.


## Comments for A4 

### Task 1: Automated Tests
Pull request: https://github.com/remla24-team10/model-training/pull/4 & https://github.com/remla24-team10/model-training/pull/6
Contributor: Jan van der Meulen & Michael Chan
The Pytest library is setup and can be found in the model-training repository under the ```tests``` folder.
Some tests such as the non-determinism tests have to be ran manually after dvc pull and are not integrated into CI.

### Task 2: Continuous Training
Pull request: https://github.com/remla24-team10/model-training/pull/5 & https://github.com/remla24-team10/model-training/pull/3
Contributer: Remi Lejeune & Shayan Ramezani
Pipeline currently automatically runs fast tests only.
We can now see the tests results on codecov
We can also see them in the actions and on the README

