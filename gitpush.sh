#!/bin/bash

if [ -z "$1" ]; then
   echo "Commit Message required"
   exit 1
fi
echo "adding changes....."
git add .
echo "committing change......"
git commit -m "$1"
echo "Pushing to Github"
git push
echo "Done Yay!"
