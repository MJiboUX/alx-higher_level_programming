#!/bin/bash
#  script that sends a POST request to the passed URL,
# and displays the body of the response
# variable email is sent with the value hr@holbertonschool.com
# variable subject is sent with value I will always be here for PLD
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
