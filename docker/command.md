- Install:
    apt install docker
    apt install docker-compose

docker run will pull and start docker image
docker run -d: run in detach mode 
docker stop [docker_container_id]
docker start [container_id]
docker run -p[HostMachine_port]:[container_port] container_name --name container_name
docker network -ls

- Docker chay:
docker network create [network_name]
docker run -d \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=root \
    -e MONGO_INITDB_ROOT_PASSWORD=example \
    --name mongo \
    --net mongo-network \
    mongo

docker run -d \
    -p 8081:8081 \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME=root \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD=example \
    --net mongo-network \
    --name mongo-express \
    -e ME_CONFIG_MONGODB_SERVER=mongo \
    mongo-express

- docker-compose:
    - https://github.com/kartheekgottipati/Docker-compose-flask-redis-deploy
    - https://www.dabbleofdevops.com/blog/setup-a-redis-python-docker-dev-stack