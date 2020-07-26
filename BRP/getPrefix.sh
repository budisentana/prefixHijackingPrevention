#!/bin/bash

# Get AS Number
vtysh -c 'show run' | grep -oP '(?<=router bgp )[^ ]*'>ASN.txt
# Get Prefix or network announced
Prefix=$(vtysh -c 'show ip bgp' | awk '{print $2}' | head -n -2 | tail -n +7)
# Get next hop
#NextHop=$(vtysh -c 'show ip bgp' | awk '{print $3}' | head -n -2 | tail -n +6 )
# Get Path
Path=$(vtysh -c 'show ip bgp' | awk '{print $6}' | head -n -2 | tail  -n +7)

# Generate Titles for table
#TITLE=$(paste -d'|' <(echo "ASN") <(echo "Prefix") <(echo "Next_Hop") <(echo "Path"))
# Generate table
LIST=$(paste -d';' <(echo "$Prefix")  <(echo "$Path")>result.txt)

# Merge titles and table
#OUTPUT=$(echo -e "$TITLE" && echo -e "$LIST")
# Display output
#echo -e ""
#echo -e "------------------------------------------------"
#echo -e "ASN Prefix and PATH"
#echo -e "------------------------------------------------"
#echo -e ""
#echo -e " $OUTPUT" | column -s'|' -t # Echo output and colmnize it
#echo -e ""


