#!/bin/bash
rm -rf .git

git init
git remote add origin git@github.com:rahul-pandare/LF-DEM_notebooks.git

git add .
git commit -m "Initial commit"
git push -u origin master
echo "Changes pushed successfully!"