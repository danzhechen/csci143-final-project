# Flask on Docker aka.Small Instagram

Welcome to Small Instagram - a web service inspired by the foundational technology stack of Instagram. This project is designed as an educational tool to provide Dockerizing Flask with Postgres, Gunicorn, and Nginx for both development and production environments.

## Overview

By following this guide, you'll deploy a simplified version of Instagram. The repository includes a configuration of Flask to run on Docker and a setup handling static and media files. The project sets the groundwork for deploying scalable web applications, mirroring the tech stack used by Instagram with an emphasis on containerization.

This project refers to this tutorial: [Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/).

## Prerequisites

Before starting, ensure you have Docker and Docker Compose installed on your machine. These tools are essential for creating and managing your containerized environment.

## Setup Instructions

### Development Environment

1. **Launching the Containers**: Build the image and run the containers.
   ```
   docker-compose up -d --build

2. **Testing out**: Make a test to see whether this webpage works.
   ```
   $ curl http://localhost:your_port_here

   You should be able to receive output similar to below.
   ```
   "hello": "world"

### Production Environment

1. **Container Depolyment**: Build the image and run the containers.
   ```
   docker-compose -f docker-compose.prod.yml up -d --build

2. **Tesing out**: Make a test to see whether this webpage works.
   ``` 
   $ curl http://localhost:your_port_here
   
   You should be able to receive output similar to below.
   ```
   "hello": "world"

### Database Initialization 

To create or reset the database tables to track the users, execute the following:

**For Development**:
```
docker-compose exec web python manage.py create_db

**For Production**:
```
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db

### Serving Static Files & Media Files

**Static Files**:
Nginx is configured to serve static files from the '/static/' path. Test this functionality by navigating to http://localhost:your_port_here/static/hello.txt.

**Media Files**:
You should be able to upload an image at http://localhost:your_port_here/upload, and then view the image at http://localhost:your_port_here/media/IMAGE_FILE_NAME.

Here is a gif showing how the process looks like. 

### Troubleshooting

Encountering network errors during shutdown may require manually stopping and removing active containers. Use commands like `docker ps` to identify running containers, followed by `docker stop <container_id>; docker rm <container_id>` to stop and remove them.
