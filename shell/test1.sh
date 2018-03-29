#!/bin/bash
cat /data/host |while read line

do
 ./expect.sh $line

done