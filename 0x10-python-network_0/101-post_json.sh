#!/bin/bash
# send JSON post request
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "${1}"
