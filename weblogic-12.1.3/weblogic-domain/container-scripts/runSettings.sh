#!/bin/bash
# Wait for AdminServer to become available for any subsequent operation
/u01/oracle/waitForAdminServer.sh

# Start Node Manager
echo "Starting NodeManager in background..."
nohup startNodeManager.sh > log.nm 2>&1 &
echo "NodeManager started."

# Add this 'Configuration' to the AdminServer only if 1st execution
wlst /u01/oracle/add-configuration.py

# print log
tail -f log.nm
