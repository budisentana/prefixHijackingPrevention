#!/bin/bash

Prefix=$(awk '{print $2}' "monitor.log" | head -n -2 | tail  -n +8)
Next_Hope=$(awk '{print $3}' "monitor.log" | head -n -2 | tail  -n +8)
Path=$(awk '{print $(NF-1)}' "monitor.log" | head -n -2 | tail  -n +8)

LIST=$(paste -d';' <(echo "$Prefix") <(echo "$Next_Hope")  <(echo "$Path")>capture.txt)



