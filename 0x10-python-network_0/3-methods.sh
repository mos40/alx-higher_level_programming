#!/bin/bash

# Takes in a URL and displays all HTTP methods the server will accept
# Usage: ./3-methods.sh <URL>

# Sending an OPTIONS request to the URL and displaying the Allow header
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d' ' -f2-
