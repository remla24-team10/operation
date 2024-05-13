# Operation

This is the main repository of [remla24-team10](https://github.com/remla24-team10)

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
docker-compose up -d
```

You can then access the wep app via: [localhost](http://localhost:5000/)

[//]: # (# This README should introduce your highlevel architecture and that links to the corresponding repositories, so visitors can easily understand your project and find all relevant information. )
