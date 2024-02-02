# Playground for [Ollama](https://ollama.ai/blog/python-javascript-libraries) and Python

```bash

[Install](https://ollama.ai/download/linux)

conda create --name ollama.play python=3.11

conda activate ollama.play

pip install pip-tools

pip-compile ./requirements.in

pip install -r ./requirements.txt

ollama run llama2

```
