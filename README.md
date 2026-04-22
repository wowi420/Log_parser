## Automated Logparser (AL)

##  INTRODUCTION
    This script are part of my learning process on python automation in GNU/Linux enviroment.
Im expected how to parse existing log from an existing tools like Journalctl and extract/count services available in set/list,
while this seems trivial but my goal here is to make a working log parser, as for finding important information i believe i could change it when i build a server.
with this i hope the code is not that bad.

#  TECH:
    -Cron
    -Python
    -subprocess
    -OS module
    -Regex

#  Note:
    This module is meant to be used for automated use by Cron not used manually 

##  INSTALLATION
1.mkdir logpapar
2.cd logpapar
3.install the repo
4.chmod 700 logparser.py

##  HOWTO IMPLEMENT THE MODULE INTO CRON
1.make sure you are in GNU/Linux enviroment, and got Cron implemented.. because this script intended for Cron
2.execute command "crontab -e", this will allow you to write a list of things Cron will do at certain situation/Time
3.you can use specific time or Extensions(@reboot,2@daily), refer on:https://man7.org/linux/man-pages/man5/crontab.5.html 
4.use the desired format and put the file location
    ex:
    @reboot home/user/script_place/script.py
5.DONE!
