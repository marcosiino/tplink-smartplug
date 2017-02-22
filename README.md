I've forked this repo from the original one to build a script to allow to export an xlsx file with the energy consumption of all my tplink smartplug devices, day by day, so that i can build charts and sum all the energy consumptions. This features is not available in the TPLink Kasa app so i had to build a script for that.


## XLSX Export Script ##

1) After cloning the repository, build the virtual environment with the needed python packages by launching ./build_venv.sh, this will create a virtual environment called venv and will install the python packages used by the script (listed in requirements.txt) inside that virtual environment

2) Activate the virtual environment by launching source venv/bin/activate

3) Edit the ip address of all the smartplug devices to export inside the export_xlsx.py (a better way will be implemented)

4) Edit the months and years to export in the dates array at the beginning of export_xlsx.py (a better way will be implemented)

5) launch python export_xlsx.py to export the xlsx file. 


## About the tplink_smartplug_module.py module ##

This is script derived from tplink-smartplug.py that can be used as python module, with a sendCommand function to send json commands to TPLink SmartPlug devices from a python script. This module is used by the xlsx export script.

#### Usage ####

`import tplink_smartplug_module`

`tplink_smartplug_module.sendCommand("ip", "jsonCommand");`

See the json commands here: [tplink-smarthome-commands.txt](tplink-smarthome-commands.txt).

