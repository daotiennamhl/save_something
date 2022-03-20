- Hỗ trợ quá trình dev, khi cài đặt môi trường
- Hỗ trợ quá trình deploy

- Each container has own port => Host machine must binding port difference for each container
- GPG key = Gnu Privacy Guard

- Compare docker, VM, OS:
    - OS: Applications, OS Kernel, Hardware
    - VM: Applications, OS Kernel
    - Docker: Applications
- Docker network:
    - docker container can communicate with each other by container name if it's in the same docker network
    - Docker compose will auto create a network for all container
    - depend_on will make container run sequently
    - volumn will make container save data will restart
- Dockerfile:
    - RUN vs CMD:
        - RUN is image build step
        - CMD is command that the container executes
        - ENTRYPOINT specifies a command that will always be executed when the container starts. The CMD specifies arguments that will be fed to the ENTRYPOINT.
        - ref: https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile

- Docker registry:
    - image naming in registry: registryDomain/imageName:tag

- Docker volume:
    - docker run -v [host_volume]:[container_volume]
    - anonymous volume: docker run -v [container_volume]
    - named volumes: docker run -v [name]:[container_volume]
    
- Kubernetes:
    - Ecosystem for managing a cluster of Docker containers while docker is container plaftform for configuring, building and distributing containers.
    