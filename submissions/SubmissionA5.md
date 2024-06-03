# Operation

This is the main repository of [remla24-team10](https://github.com/remla24-team10)
Operation: https://github.com/remla24-team10/operation/tree/main

Relevant versions have been tagged with tag "a5"

The README file contains the architecture, installations and comments for each assignments.



## Comments for A5

### Task 1: Traffic Management
Pull request: https://github.com/remla24-team10/operation/pull/9 & https://github.com/remla24-team10/operation/pull/4
Contributor: Michael Chan & Shayan Ramezani
The project now utilises the istio service mesh for requests and compatible with ansible. Dashboards are not yet visible on host when using vagrant VM + ansible.
### Task 2: Continuous Experimentation
Pull request: https://github.com/remla24-team10/operation/pull/13 & https://github.com/remla24-team10/app/pull/4
Contributor: Remi Lejeune & Jan van der Meulen
Two app versions have been created and are served on a 50/50 basis via istio. This can be set to 90/10 later but 50/50 makes it easier to test, additionally the prometheus update interval is set to 1s for the same reason.
### Task 3: Additional Use Case 
Pull request: https://github.com/remla24-team10/operation/pull/12
Contributor: Michael Chan
Rate limits were implemented. The rate limit is set to 20 requests per minute for each page version.