#!/usr/bin/env bash

echo "What's your commit message: "
read message

git add .
git commit -m "$message"
git push
