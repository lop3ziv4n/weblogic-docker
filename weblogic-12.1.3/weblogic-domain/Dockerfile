# HOW TO BUILD THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-domain:12.1.3  --build-arg ADMIN_PASSWORD=example .

# Pull base image
FROM app/weblogic-install:12.1.3

# Argument variable
ARG ADMIN_PASSWORD="app2016"

# Environment variables required for this build
ENV DOMAIN_NAME="base_domain" \
    DOMAIN_HOME="/u01/oracle/user_projects/domains/base_domain" \
    ADMIN_PORT="8001" \
    ADMIN_HOST="wlsadmin" \
    NM_PORT="5556" \
    MS_PORT="7001" \
    CLUSTER_NAME="DockerCluster" \
    CONFIG_JVM_ARGS="-Dweblogic.security.SSL.ignoreHostnameVerification=true" \
    PATH=$PATH:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/user_projects/domains/base_domain/bin:/u01/oracle

# Add files required to build this image
COPY container-scripts/* $ORACLE_HOME/

# Configuration of WLS Domain
RUN /u01/oracle/wlst /u01/oracle/create-wls-domain.py && \
    mkdir -p /u01/oracle/user_projects/domains/base_domain/servers/AdminServer/security && \
    echo "username=weblogic" > /u01/oracle/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \ 
    echo "password=$ADMIN_PASSWORD" >> /u01/oracle/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
    echo ". /u01/oracle/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /u01/oracle/.bashrc && \ 
    echo "export PATH=$PATH:/u01/oracle/wlserver/common/bin:/u01/oracle/user_projects/domains/base_domain/bin" >> /u01/oracle/.bashrc && \
    cp /u01/oracle/commEnv.sh /u01/oracle/wlserver/common/bin/commEnv.sh && \
    rm /u01/oracle/create-wls-domain.py /u01/oracle/jaxrs2-template.jar 

# Parameters app of domain
RUN sed -i 's/JAVA_OPTIONS\=\"\${JAVA_OPTIONS} \${JAVA_PROPERTIES}\"/JAVA_OPTIONS\=\"\${JAVA_OPTIONS} \${JAVA_PROPERTIES} -Xms4096m -Xmx6144m -XX:PermSize\=256m -XX:MaxPermSize\=1024m -XX:CompileThreshold\=8000 -Denv\=local -Denvironment\=local -Dserver.home\=\/u01\/oracle -Dprops.path\=\/u01\/oracle\/properties -DenableLogger\=\/u01\/oracle\/properties\/\"/g' $DOMAIN_HOME/bin/setDomainEnv.sh
#RUN sed -i '6i\MEM_ARGS=\"-Xms4096m -Xmx6144m -XX:PermSize\=256m -XX:MaxPermSize\=1024m\"' /u01/oracle/user_projects/domains/base_domain/startWebLogic.sh

USER oracle
WORKDIR $ORACLE_HOME

# Define default command to start bash.
CMD ["bash"]
