# HOW TO BUILD THIS IMAGE
# -----------------------
# Build:
#      $ docker build -t app/jdk:7 .

# Pull base image
FROM oraclelinux:latest

# Environment variables required for this build
ENV JAVA_PKG=server-jre-7u*-linux-x64.tar.gz \
    JAVA_HOME=/usr/java/default \
    PATH=$PATH:/usr/java/default/bin

# Add files required to build this image
ADD download/$JAVA_PKG /usr/java/

RUN mv $(ls -1 -d /usr/java/*) $JAVA_HOME 