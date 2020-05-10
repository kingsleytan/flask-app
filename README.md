# Flask App: Create SaaS Software
An application to create SaaS-based software with Flask, Python, Docker, gunicorn, celery.

## Docker
### First time docker build
`docker-compose --build`

### Subsequent up Docker server
`docker-compose up`

### To stop Docker server
`docker-compose stop`

### To remove docker compose image
`docker-compose rm -f`

### To remove dangling docker image
`docker rmi -f $(docker images -qf dangling=true)`