#!/usr/bin/bash

# ---Colours---
RED='\e[31m'
BOLD='\e[1m'
NC='\e[0m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'

# ------------------------------------------------------------------Main Code--------------------------------------------------------------
ping -c 4 www.google.com > /dev/null
status=$?

# ---Main if/else Block
if [[ $status -eq 0 ]]; then
   printf "${GREEN}Connected to the internet.${NC}\n"
elif [[ $status -ne 0 ]]; then
   printf "${RED}Cannot reach the internet, do you want to connect to a network(y/n).${NC}"
   read -p "" response
   response="${response,,}"
   
#---Decision making with string inputs--- 
   if [[ $response == 'y' ]]; then
      nmcli device wifi list
      read -p "Enter your SSID: " ssid
      sudo nmcli device wifi connect "${ssid}" --ask
   elif [[ $response == 'n' ]]; then
      printf "${YELLOW}Exiting...${NC}\n"
      exit 0
   fi

fi

