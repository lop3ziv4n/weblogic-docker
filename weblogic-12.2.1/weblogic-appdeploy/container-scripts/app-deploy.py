# WLST Offline for deploying an application located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default

import os

# Deployment Information 
domainHome = os.environ.get('DOMAIN_HOME')
clusterName = os.environ.get('CLUSTER_NAME')
appPath = os.environ.get('APP_PKG_LOCATION')

# Read Domain in Offline Mode
readDomain(domainHome)

for fileNames in os.listdir(appPath):
    (fileName, fileExtension) = os.path.splitext(fileNames)
    if fileExtension == '.war':
        print("AppDeployment: " + fileName + fileExtension)
        # Create Application
        cd('/')
        app = create(fileName, 'AppDeployment')
        app.setSourcePath(appPath + '/' + fileName + fileExtension)
        app.setStagingMode('nostage')
        # Assign application to AdminServer
        assign('AppDeployment', fileName, 'Target', 'AdminServer')
        assign('AppDeployment', fileName, 'Target', clusterName)

# Update Domain, Close It, Exit
updateDomain()
closeDomain()
exit()
