# Operation

This is the main repository of [remla24-team10](https://github.com/remla24-team10)
Operation: https://github.com/remla24-team10/operation/tree/main

Relevant versions have been tagged with tag "a3"

The README file contains the architecture, installations and comments for each assignments.


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
- Docker compose was migrated to minikube, both methods of running the containers still work. minikube utilises ingresses but still requires minikube tunnel to the ingress.
### Task 4: App Monitoring & Grafana
Pull request: https://github.com/remla24-team10/app/pull/3 & https://github.com/remla24-team10/operation/pull/6
Contributor: Michael Chan
Reviewer: Remi Lejeune
- Prometheus ServiceMonitor was used to collect metrics, which includes 2 gauges and a counter. A grafana json file was included in the repository which can be imported in grafana, it contains a dashboard with 3 panels.