# Apache Web Server with WebLogic plugin for load balancing WebLogic on Docker Containers

# HOW TO BUILD AND RUN THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/apache-webtier .
# Run:
#      $ docker run -d --link wlsadmin:wlsadmin -e WEBLOGIC_CLUSTER=wlsadmin:8001 -p 80:80 app/apache-webtier

# Pull base image
FROM httpd:2.4

# Environment variables required for this build
ENV PLUGIN_PKG="WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64.zip" \
    PLUGIN_HOME="/root" \
    MOD_WLS_PLUGIN="mod_wl_24.so" \
    LD_LIBRARY_PATH="/root/lib" \
    WEBLOGIC_CLUSTER="server0:7001,server1:7001" \
    APACHE_HOME="/usr/local/apache2"

# Add files required to build this image
COPY container-scripts/* $PLUGIN_HOME/
COPY download/* $PLUGIN_HOME/

# Install and configure Apache Web Server with WebLogic
RUN apt-get update && apt-get install -y unzip && \
    unzip /root/$PLUGIN_PKG -d $PLUGIN_HOME && \
    cat /root/weblogic.conf >> $APACHE_HOME/conf/httpd.conf && \
    rm /root/$PLUGIN_PKG /root/weblogic.conf