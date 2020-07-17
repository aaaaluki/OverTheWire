#!/bin/bash

echo "Enter comit message:"
read commit_msg

git add *
git commit -m "$commit_msg"

branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
git push -u origin $branch

echo "Save+Push script finished!"
