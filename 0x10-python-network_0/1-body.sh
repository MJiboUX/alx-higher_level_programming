#!/bin/bash
# script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
# display only body of a 200 status code response
# used curl
curl -sLf $1
