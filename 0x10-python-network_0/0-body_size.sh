#!/usr/bin/env bash
# cURL body size
curl -sI "$1" | grep -i Content-Length | awk -F ' ' '{print $2}'
