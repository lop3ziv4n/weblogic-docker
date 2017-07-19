# HOW TO BUILD THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-install .

# Pull base image
FROM app/jdk:8

# Environment variables required for this build (do NOT change)
ENV FMW_PKG=fmw_12.2.1.0.0_wls_quick_Disk1_1of1.zip \
    FMW_JAR=fmw_12.2.1.0.0_wls_quick.jar \
    ORACLE_HOME=/u01/oracle \
    USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom" \
    PATH=$PATH:/usr/java/default/bin:/u01/oracle/oracle_common/common/bin

# Add files required to build this image
COPY container-scripts/* /u01/
COPY download/* /u01/

# Setup filesystem and oracle user
# Install and configure Oracle JDK
# Adjust file permissions, go to /u01 as user 'oracle' to proceed with WLS installation
RUN chmod a+xr /u01 && \
    useradd -b /u01 -m -s /bin/bash oracle && \
    echo oracle:oracle | chpasswd && \
    cd /u01 && $JAVA_HOME/bin/jar xf /u01/$FMW_PKG && cd - && \
    su -c "$JAVA_HOME/bin/java -jar /u01/$FMW_JAR -invPtrLoc /u01/oraInst.loc -jreLoc $JAVA_HOME -ignoreSysPrereqs -force -novalidation ORACLE_HOME=$ORACLE_HOME" - oracle && \
    chown oracle:oracle -R /u01 && \
    rm /u01/$FMW_JAR /u01/$FMW_PKG /u01/oraInst.loc /u01/install.file

USER oracle
WORKDIR $ORACLE_HOME 

# Define default command to start bash. 
CMD ["bash"]
