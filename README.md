# hackfestival-schwarz-it-challenge

## Getting Started



### Start using Docker

```
docker-compose -f docker/docker-compose.yml up
```

## Native Install

### Ubuntu
```
sudo apt-get install libpq-dev
```

### MacOS

```
brew install postgresql
```

### Install Packages

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r backend/requirements.yml
```

# Ask chatGPT

```
export OPENAI_API_KEY="ask alex for a token"
python lllm/ask_chatGPT.py
```