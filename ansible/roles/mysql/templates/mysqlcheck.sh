#!/bin/bash

state=$(systemctl show -p ActiveState mysql | sed 's/ActiveState=//g')
if [[ $state != 'active' ]]; then
    logger System "mysql restarted by fail-check script"
    systemctl restart mysql.service
fi
