#!/bin/bash

# Sends a DELETE request to the given URL and displays the body of the response
# Usage: ./2-delete.sh <URL>
# Sending a DELETE request to the URL and displaying the response body
curl -sX DELETE $1 -L
