# HOW TO BUILD AND RUN THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-appdeploy:12.1.3  --build-arg ADMIN_PASSWORD=example .
# Run:
#	   $ docker run -d -p 8001:8001 app/weblogic-appdeploy:12.1.3  --name app-weblogic
#                                       -v /path/host/example/properties:/u01/oracle/properties
#                                       -v /path/host/example/webapps:/u01/oracle/webapps
#                                       -v /path/host/example/logs:/u01/oracle/logs
#                                       -v /path/host/example/logs:/u01/oracle/user_projects/domains/base_domain/servers/AdminServer/logs
#
# To start a Managed Server to self-register with the Admin Server above, run:
#   Start Node Manager, create a Machine, and create a Managed Server automatically:
#        $ docker run -d --name=app-weblogic-ms1 --link app-weblogic:app-weblogic -p 7001:7001 app/weblogic-appdeploy:12.1.3 createServer.sh
#   Start Node Manager and create a Machine automatically:
#        $ docker run -d --name=app-weblogic-m1 --link app-weblogic:app-weblogic -p 7001:7001 app/weblogic-appdeploy:12.1.3 createMachine.sh
#

# Pull base image
FROM app/weblogic-domain

# Environment variables required for this build
ENV APP_PKG_LOCATION /u01/oracle/webapps

# Add files required to build this image
USER oracle
COPY container-scripts/* /u01/oracle/

# Add application for deploying
COPY appdeploy/* $APP_PKG_LOCATION/

# Copy files and deploy application in WLST Offline mode
RUN wlst /u01/oracle/app-deploy.py
