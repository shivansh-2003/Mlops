# Dockers 

## Introduction
Docker is a platform that enables developers to automate the deployment of applications inside lightweight, portable containers. This README provides an overview of basic Docker commands to help you get started.

## Installation
To install Docker, follow the instructions for your operating system on the [official Docker installation page](https://docs.docker.com/get-docker/).

## Basic Commands

### 1. **docker --version**
Check the installed version of Docker.
```
docker --version
```

### 2. **docker pull**
Download a Docker image from Docker Hub.
```
docker pull <image_name>
```


### 3. **docker images**
List all downloaded Docker images.
```
docker images
```

### 4. **docker run**
Run a command in a new container.
```
docker run <options> <image_name> <command>
```
### 5. **docker ps**
List running containers.
```
docker ps
```