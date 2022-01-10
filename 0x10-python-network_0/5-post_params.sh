#!/bin/bash
# post parameters
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
