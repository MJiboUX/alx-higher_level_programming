#!/bin/bash
# Bash script that sends a request to a URL passed as an argument,
# displays only the status code of the response
# not used any pipe, redirection, etc.
# not used ; and &&
curl -s "$1" -o /dev/null -w "%{http_code}"
