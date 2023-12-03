#!/bin/bash
# Script that sends a POST request and displays the body response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
