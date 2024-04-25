#!/bin/bash
# Bash script that takes in a URL,
# sends a request to that URL,
# and displays the size of the body of the response
url=$1
body_size=$(curl -sI $url | grep -i Content-Length | awk '{print $2}')
if [ -z "$body_size" ]; then
    echo "Error: Couldn't fetch content size"
else
    echo $body_size
fi
