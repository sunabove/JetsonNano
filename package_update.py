#!/usr/bin/python3

cmds = """
# package update #
# sudo vi /var/lib/dpkg/status
# sudo vi /var/lib/dpkg/available

sudo apt install python3-pip -y

sudo apt install python-is-python3  -y

sudo apt install build-essential libdbus-glib-1-dev libgirepository1.0-dev  -y

sudo apt install gettext -y

sudo apt install librsync-dev -y

sudo apt install libcairo2-dev -y

sudo apt install libsystemd-dev -y

sudo pip3 install dbus-python

sudo pip3 install pipdate

sudo python3 -m pip install pip --upgrade

sudo -H pipdate

sudo ubuntu-drivers autoinstall

#sudo apt install nvidia-cuda-toolkit -y

#sudo apt install nvidia-utils-510 -y

#sudo pip3 install torch torchvision torchaudio

sudo apt autoremove -y

"""

import os 

cmds = cmds.strip().splitlines()

for idx, cmd in enumerate( cmds ) :
    cmd = cmd.strip()

    if len( cmd ) == 0 :
        continue
    elif cmd.startswith( "#" ) :
        continue
    pass

    if idx : print()

    print( cmd, flush=1 )

    #result = os.popen( cmd ).read()

    #print( result, flush = 1 )

    os.system( cmd )
pass
