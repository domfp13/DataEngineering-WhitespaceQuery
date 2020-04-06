#!/bin/bash
. ~/.bash_profile
#################################################
#
#  This is the bash script that is being run by 
#  cron and runs DataEngineering-QueryRunner 
#  
#
#  Change History
#  --------------------------------
#  Luis Fuentes initial
#################################################

# Deletting 
cd /home/dbirptng/marodrig/DataEngineering-WhitespaceAnalysis/uploads/
rm -rf *
# running Whitespace_usa
cd /ishome/ssg/lf188653/projects/DataEngineering-WhitespaceQuery/
/ishome/ssg/lf188653/.conda/envs/testenv/bin/python main.py whitespace_usa