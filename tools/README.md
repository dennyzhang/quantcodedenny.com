# setup env
```
# use docker

docker build -t denny-llm-stock-base .

export MY_GEMINI_API_KEY="sk-xxx"
docker run -e gemini_api_key="$my_gemini_api_key" denny-llm-stock-base
```

# sample run
```
bash-3.2$ export MY_GEMINI_API_KEY="XXX"
bash-3.2$ docker run -e GEMINI_API_KEY="$MY_GEMINI_API_KEY" denny-llm-stock-base
hi there
```
