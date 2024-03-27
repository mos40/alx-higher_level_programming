#!/bin/bash

# Sends a request to the given URL and displays the size of the body of the response
# Usage: ./0-body_size.sh <URL>
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sX GET $1 -L
