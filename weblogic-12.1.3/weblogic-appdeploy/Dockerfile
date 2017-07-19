# HOW TO BUILD AND RUN THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-appdeploy:12.1.3 .

# Pull base image
FROM app/weblogic-domain:12.1.3

# Environment variables required for this build
ENV APP_PKG_LOCATION /u01/oracle/autodeploy

# Add files required to build this image
COPY container-scripts/* $ORACLE_HOME/

# Add application for deploying
RUN mkdir -p $APP_PKG_LOCATION
COPY appdeploy/* $APP_PKG_LOCATION/

# Copy files and deploy application in WLST Offline mode
RUN $ORACLE_HOME/wlst $ORACLE_HOME/app-deploy.py

USER oracle
WORKDIR $ORACLE_HOME

# Define default command to start bash.
CMD ["bash"]