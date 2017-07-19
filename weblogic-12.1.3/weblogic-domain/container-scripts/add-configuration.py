# Script to create and add a new configuration automatically to the domain's AdminServer running on 'wlsadmin'

import os

execfile('/u01/oracle/commonfuncs.py')

# Deployment Information
domainName = os.environ.get('DOMAIN_NAME', 'base_domain')
timeoutSeconds = '120'
abandonTimeoutSeconds = '120'

# Connect to the AdminServer
connectToAdmin()

# Create a Machine
editMode()

# Set the JTA configuration
print("JTA Configuration")
cd('/JTA/' + domainName)
set('TimeoutSeconds', timeoutSeconds)
set('AbandonTimeoutSeconds', abandonTimeoutSeconds)

saveActivate()

# Exit
exit()

