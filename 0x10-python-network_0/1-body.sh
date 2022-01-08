#!/bin/bash
# sends GET request to the URL and displays the body of the response
curl -sf "$1" -X GET
