#!/bin/sh
sudo docker build -t ghcr.io/ziro-bot/randomapi . \
&& sudo docker push ghcr.io/ziro-bot/randomapi:latest
