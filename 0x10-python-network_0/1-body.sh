#!/bin/bash
# sends GET request to the URL and displays the body of the response
curl -sfL "$1" -X GET
