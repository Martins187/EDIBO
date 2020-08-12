#!/bin/bash

git add .
read -p "Faila nosaukums: " x
git commit -m $x
git push origin

