#!/bin/bash

cp /Users/Cheng/Documents/Dal/Fall\ 2015/Co-op/Résumé.pdf ./static/resume.pdf 
git add .
git commit -m "$1"
git push 
