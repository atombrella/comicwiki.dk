#!/bin/bash

git  remote  set-branches  --add  origin  REL1_39
git  fetch   origin
git  checkout -b REL1_39 origin/REL1_39

composer update

cd maintenance
php update.php

# do the other magic stuff with new files etc.
