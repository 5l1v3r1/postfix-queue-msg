#!/bin/bash

# @dalvarez_s 2016/03/07
# Email hold messages in Postfix queue (Due to ClamAV detection)

for email in `mailq | grep -e "[0-9A-Z]*\!" | awk -F'!' '{print $1}'`; do postcat -q $email > $email.txt; done
for email in `ls *.txt`; do zip -P infected $email.zip $email; python pysendemail.py "to@to.com" "from@from.com" "Subject" "Message Text" $email.zip; rm $email $email.zip; postsuper -d ${email:0:${#email}-4}; done 

