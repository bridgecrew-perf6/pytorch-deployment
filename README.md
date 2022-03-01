# Pytorch inference API

## Running locally

```shell
make venv
make install
make run
```

## Running docker

```shell
docker build -t pytorch-deployment .
docker run -ti -p 8000:8000 pytorch-deployment
```