FROM centos:centos7
MAINTAINER Flavia Saplacan <flavia.saplacan@gmail.com>

# Mongodb install
RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install mongodb-server; yum clean all
RUN mkdir -p /data/db


# Pip install
RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all

# Add current path inside docker
ADD app /app


# Install pip dependencies
RUN pip install -r /app/requirements.txt

# Move to working dir
WORKDIR /app

