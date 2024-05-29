# Operation

This is the main repository of [remla24-team10](https://github.com/remla24-team10)
Operation: https://github.com/remla24-team10/operation/tree/main

Relevant versions have been tagged with tag "a4"

The README file contains the architecture, installations and comments for each assignments.


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