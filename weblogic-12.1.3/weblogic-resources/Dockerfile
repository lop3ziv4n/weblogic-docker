# HOW TO BUILD AND RUN THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-resources:12.1.3 .

# Pull base image
FROM app/weblogic-domain:12.1.3

# Add files required to build this image
COPY container-scripts/* $ORACLE_HOME/

# Copy files and deploy application in WLST Offline mode
RUN $ORACLE_HOME/wlst -loadProperties $ORACLE_HOME/datasource.properties $ORACLE_HOME/ds-deploy.py && \
    $ORACLE_HOME/wlst $ORACLE_HOME/jms-deploy.py

USER oracle
WORKDIR $ORACLE_HOME

# Define default command to start bash.
CMD ["bash"]