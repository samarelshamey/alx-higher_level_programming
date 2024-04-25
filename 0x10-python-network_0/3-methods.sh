#!/bin/bash
# display all http method the server accept
curl -s -i -L -X "${1}"
