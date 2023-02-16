import config
import os
import docker

docker_client = docker.from_env()

config.logger.info("Removing stopped containers")
docker_client.containers.prune()

config.logger.info("Creating iot-thing image")


docker_client.images.build(
    path="../docker",
    dockerfile="Dockerfile",
    tag="iot-thing-aws"
)

config.logger.info("Get all the data file")
data_files = os.scandir("../docker/data")
    
config.logger.info("Creating iot-thing container")

for thing in os.scandir("../docker/certificates"):
    docker_client.containers.run(
        image="iot-thing-aws",
        environment={"CLIENT_ID" : thing.name},
        volumes={
            str(os.path.abspath(thing)): {'bind': '/certificates', 'mode': 'ro'},
            str(os.path.abspath(next(data_files))) : {'bind':'/data/data.jsonl.gz', "mode":"ro"}},
        detach=True)