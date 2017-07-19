# Script to create and add NodeManager automatically to the domain's AdminServer running on '$ADMIN_HOST'.
# =============================
import os
import socket

execfile('/u01/oracle/commonfuncs.py')

# NodeManager details
nmhost = os.environ.get('NM_HOST', socket.gethostbyname(hostname))
nmport = os.environ.get('NM_PORT', '5556')

# Connect to the AdminServer
connectToAdmin()

# Create a Machine
editMode()

cd('/')
cmo.createMachine(nmname)
cd('/Machines/' + nmname +'/NodeManager/' + nmname)
cmo.setListenPort(int(nmport))
cmo.setListenAddress(nmhost)
cmo.setNMType('Plain')

saveActivate()

# Exit
exit()
