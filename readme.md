# Playground for [Ollama](https://ollama.ai/blog/python-javascript-libraries) and Python

Notes on an initial play with Ollama.

## Setting up the engine

The engine can be [installed](https://ollama.ai/download/linux) on the host.

And run-up a model using the following command:

`ollama run llama2`

Alternatively it can be spun up in a docker container using the following command:

`docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

To pull down a model in a container:

`docker exec -it ollama ollama pull mistral`

On a container rup-up the model in the container:

`docker exec -it ollama ollama run llama2`

And to start the container (if required after restart):

`docker start ollama`

To view the logs in the container:

`docker logs -f ollama`

## Application Development

Prerequisites were to create a environment using [Anaconda](https://www.anaconda.com/):

`conda create --name ollama.play python=3.11`

And then it can be enabled using the following command:

`conda activate ollama.play`

Load in the dependencies in the `src` folder using the following commands:

```bash
pip install pip-tools

pip-compile ./requirements.in

pip install -r ./requirements.txt
```

## Benchmarks

Snapshot of times taken by various models (in seconds).

|Model|Instruction|Training and Validation|
|-|-|-|
|llama2|87.8539|1161.0374|
|mistral|54.3922|1172.8433|
