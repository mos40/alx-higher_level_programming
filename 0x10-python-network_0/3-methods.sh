#!/bin/bash

# Takes in a URL and displays all HTTP methods the server will accept
# Usage: ./3-methods.sh <URL>
# Sending an OPTIONS request to the URL and displaying the Allow header
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
