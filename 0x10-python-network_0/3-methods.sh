#!/bin/bash
# display all http method the server accept
curl -s -i -L -X OPTIONS "${1}" | grep "^Allow: .*"
