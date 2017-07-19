# HOW TO BUILD THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/weblogic-install:12.1.3 .

# Pull base image
FROM app/jdk:7

# Environment variables required for this build (do NOT change)
ENV FMW_JAR=fmw_12.1.3.0.0_wls.jar \
    ORACLE_HOME=/u01/oracle \
    USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom" \
    PATH=$PATH:/usr/java/default/bin:/u01/oracle/oracle_common/common/bin

# Add files required to build this image
COPY container-scripts/* /u01/
COPY download/* /u01/

# Setup required packages, filesystem, and oracle user.
# Install and configure Oracle JDK
# Adjust file permissions, go to /u01 as user 'oracle' to proceed with WLS installation
RUN chmod a+xr /u01 && \
    useradd -b /u01 -m -s /bin/bash oracle && \
    echo oracle:oracle | chpasswd && \
    su -c "$JAVA_HOME/bin/java -jar /u01/$FMW_JAR -ignoreSysPrereqs -novalidation -silent -responseFile /u01/install.file -invPtrLoc /u01/oraInst.loc -jreLoc $JAVA_HOME ORACLE_HOME=$ORACLE_HOME" - oracle && \
    chown oracle:oracle -R /u01 && \
    rm /u01/$FMW_JAR /u01/oraInst.loc /u01/install.file

USER oracle
WORKDIR $ORACLE_HOME

# Define default command to start bash. 
CMD ["bash"]
