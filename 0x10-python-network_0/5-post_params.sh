#!/bin/bash
# variable email sent with value hr@holbertonschool.com
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
