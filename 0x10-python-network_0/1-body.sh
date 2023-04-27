#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response if status code is 200
curl -sL "$1" -X GET -H "Content-Type: application/json" -w "%{http_code}" -o /dev/null | grep 200 && curl -sL "$1"
