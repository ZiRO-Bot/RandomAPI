#!/bin/sh
sudo docker build -t ghcr.io/ziro-bot/randomapi -t ghcr.io/ziro-bot/randomapi:1.0.0 . \
&& sudo docker push ghcr.io/ziro-bot/randomapi:latest \
&& sudo docker push ghcr.io/ziro-bot/randomapi:1.0.0
