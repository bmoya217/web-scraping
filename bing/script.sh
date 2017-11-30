#!/bin/bash
HOSTS="bolt.cs.ucr.edu hammer.cs.ucr.edu"
SCRIPT="pwd"
for HOST in ${HOSTS} ; do
    sshpass -p "Recursion1!" ssh -o StrictHostKeyChecking=no bmoya001@${HOST} "${SCRIPT}"
done

