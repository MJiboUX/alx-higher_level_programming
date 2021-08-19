#!/bin/bash
# Bash script that sends a JSON POST as the first argument, and displays body
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2" 
