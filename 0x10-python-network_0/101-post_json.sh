#!/bin/bash
# Bash script that sends a JSON POST request to an URL passed as the first argument and displays the body of the request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
