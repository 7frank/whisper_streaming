

# Get IP of k3d cluster
getIpCommand = "docker network inspect k3d-msl-local-dev | grep -m 1 \"Gateway\" | awk -F '\"' '{print $4}'"
hostK3dInternal = str(local(getIpCommand)).replace("\n", "")
## hostK3dInternal = "0.0.0.0" FIXME ip not exposed on macos
print("host.k3d.internal", hostK3dInternal)

docker_build(
    "ecosystem/stt",
    context=".",
    dockerfile="./docker/Dockerfile",
    ignore=[
      
    ],
    live_update=[
        sync(".", "/app")
    ],
)

k8s_yaml("./docker/deployment.yaml")

k8s_resource("stt-svc",port_forwards='8180:43007')


# Define your Docker Hub repository
docker_hub_repo = "frank1147/stt-svc"

# docker images | grep "localhost:36269/ecosystem_stt" | head -n 1 | awk '{{print $3}}' | xargs -I {{}} \

local_resource(
    name="push-stt-svc-dockerhub",
    cmd="""
    docker images | grep "localhost:36269/ecosystem_stt" | head -n 1 | awk '{{print $3}}' | xargs -I {{}} \
    docker tag {{}} {0}:latest && \
    docker push {0}:latest
    """.format(docker_hub_repo),
    auto_init=False,
    trigger_mode=TRIGGER_MODE_MANUAL

)