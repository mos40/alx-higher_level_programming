#!/bin/bash

# Sends a request to the given URL and displays the size of the body of the response
# Usage: ./0-body_size.sh <URL>

# Sending a GET request to the URL and writing the response body to a temporary file
curl -s "$1" -o temp_body

# Getting the size of the body in bytes
body_size=$(wc -c < temp_body)

# Displaying the size of the body
echo "$body_size"

# Removing the temporary file
rm temp_body
