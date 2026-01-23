#!/bin/bash

# git pull origin main
state=`git remote -v | grep upstream | wc -l`
if [ "$state" -lt 1 ]
then
    echo "Adding upstream connection"
    git remote add upstream https://github.com/ksiller/ds2002-course.git
fi

git switch main && git fetch upstream && git merge upstream/main
clear
echo "Sync of main branch with DS2002 course repository complete."
