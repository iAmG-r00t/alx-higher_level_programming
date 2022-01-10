#!/bin/bash
# send a request and only show the status code
curl -s -o /dev/null -I --w "%{http_code}" "$1"
