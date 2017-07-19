# HOW TO BUILD AND RUN THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-domain --build-arg ADMIN_PASSWORD=example .
# Run:
#	   $ docker run -d -p 8001:8001 app/weblogic-domain --name app-weblogic
#                                       -v /path/host/example/properties:/u01/oracle/properties
#                                       -v /path/host/example/webapps:/u01/oracle/webapps
#                                       -v /path/host/example/logs:/u01/oracle/logs
#                                       -v /path/host/example/logs:/u01/oracle/user_projects/domains/base_domain/servers/AdminServer/logs
#
# To start a Managed Server to self-register with the Admin Server above, run:
#   Start Node Manager, create a Machine, and create a Managed Server automatically:
#        $ docker run -d --name=appms1 --link app-weblogic:app-weblogic -p 7001:7001 app/weblogic-domain createServer.sh
#   Start Node Manager and create a Machine automatically:
#        $ docker run -d --name=appm1 --link app-weblogic:app-weblogic -p 7001:7001 app/weblogic-domain createMachine.sh

# Pull base image
FROM app/weblogic-install

# Argument variable
ARG ADMIN_PASSWORD="app2016"

# Environment variables required for this build
ENV DOMAIN_NAME="base_domain" \
    DOMAIN_HOME="/u01/oracle/user_projects/domains/base_domain" \
    ORACLE_HOME=/u01/oracle \
    ADMIN_PORT="8001" \
    ADMIN_HOST="wlsadmin" \
    NM_PORT="5556" \
    MS_PORT="7001" \
    CLUSTER_NAME="DockerCluster" \
    CONFIG_JVM_ARGS="-Dweblogic.security.SSL.ignoreHostnameVerification=true" \
    PATH=$PATH:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/user_projects/domains/base_domain/bin:/u01/oracle

# Add files required to build this image
USER oracle
COPY container-scripts/* $ORACLE_HOME/

# Configuration of WLS Domain
RUN /u01/oracle/wlst /u01/oracle/create-wls-domain.py && \
    mkdir -p /u01/oracle/user_projects/domains/base_domain/servers/AdminServer/security && \
    echo "username=weblogic" > /u01/oracle/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
    echo "password=$ADMIN_PASSWORD" >> /u01/oracle/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
    echo ". /u01/oracle/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /u01/oracle/.bashrc && \
    echo "export PATH=$PATH:/u01/oracle/wlserver/common/bin:/u01/oracle/user_projects/domains/base_domain/bin" >> /u01/oracle/.bashrc

# Parameters app of domain
RUN sed -i 's/JAVA_OPTIONS\=\"\${JAVA_OPTIONS} \${JAVA_PROPERTIES}\"/JAVA_OPTIONS\=\"\${JAVA_OPTIONS} \${JAVA_PROPERTIES} -Xms3072m -Xmx3072m -XX:PermSize\=512m -XX:MaxPermSize\=2048m -XX:CompileThreshold\=8000 -Denv\=local -Denvironment\=local -Dserver.home\=\/u01\/oracle -Dprops.path\=\/u01\/oracle\/properties -DenableLogger\=\/u01\/oracle\/properties\/\"/g' $DOMAIN_HOME/bin/setDomainEnv.sh
#RUN sed -i '6i\MEM_ARGS=\"-Xms3072m -Xmx3072m -XX:PermSize\=512m -XX:MaxPermSize\=2048m -XX:CompileThreshold\=8000\"' /u01/oracle/user_projects/domains/base_domain/startWebLogic.sh

# Volumes from native host
RUN mkdir -p $ORACLE_HOME/properties && \
    mkdir -p $ORACLE_HOME/webapps && \
    mkdir -p $ORACLE_HOME/logs
VOLUME ["$ORACLE_HOME/properties", "$ORACLE_HOME/webapps", "$ORACLE_HOME/logs" , "$DOMAIN_HOME/servers/AdminServer/logs"]

# Expose Node Manager default port, and also default for admin and managed server 
EXPOSE $NM_PORT $ADMIN_PORT $MS_PORT

WORKDIR $DOMAIN_HOME

# Define default command to start bash. 
CMD ["startWebLogic.sh"]
