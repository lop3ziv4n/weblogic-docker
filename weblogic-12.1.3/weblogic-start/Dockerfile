# HOW TO BUILD AND RUN THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic:12.1.3 .
# Run:
#	   $ docker run -d -p 8001:8001 app/weblogic:12.1.3  --name app-weblogic
#                                       -v /path/host/example/properties:/u01/oracle/properties
#                                       -v /path/host/example/webapps:/u01/oracle/webapps
#                                       -v /path/host/example/logs:/u01/oracle/logs
#                                       -v /path/host/example/logs:/u01/oracle/user_projects/domains/base_domain/servers/AdminServer/logs
#
# To start a Managed Server to self-register with the Admin Server above, run:
#   Start Node Manager, create a Machine, and create a Managed Server automatically:
#        $ docker run -d --name=app-weblogic-ms1 --link app-weblogic:app-weblogic -p 7001:7001 ehcos/weblogic:12.1.3 createServer.sh
#   Start Node Manager and create a Machine automatically:
#        $ docker run -d --name=app-weblogic-m1 --link app-weblogic:app-weblogic -p 7001:7001 app/weblogic:12.1.3 createMachine.sh
#

# Pull base image
FROM app/weblogic-appdeploy:12.1.3

# Volumes from native host
RUN mkdir -p $ORACLE_HOME/properties && \
    mkdir -p $ORACLE_HOME/webapps && \
    mkdir -p $ORACLE_HOME/logs
VOLUME ["$ORACLE_HOME/properties", "$ORACLE_HOME/webapps", "$ORACLE_HOME/logs" , "$DOMAIN_HOME/servers/AdminServer/logs"]

# Expose Node Manager default port, and also default http/https ports for admin console
EXPOSE $NM_PORT $ADMIN_PORT $MS_PORT

USER oracle
WORKDIR $DOMAIN_HOME

# Define default command to start bash.
CMD ["startWebLogic.sh"]