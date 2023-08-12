#!/bin/bash
# set up script for the bogo pi project

# checking for logs dir
if [ ! -d 'logs' ];
then
  mkdir logs
fi

# checking for python 3

if [[ ! "$(python3 -V)" =~ "python 3"]]
then
  echo "Please install Python 3"
fi