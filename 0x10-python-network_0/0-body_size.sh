#!/bin/bash
# script that takes displays the size of the body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
