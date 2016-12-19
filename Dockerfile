FROM centos:7
MAINTAINER roddy <roddy.gonzalez@schibsted.cl>

# Install python dependencies
RUN yum install -y epel-release
RUN yum install -y python34 python34-pip
RUN yum clean all

# Install pip packages
ADD requirements.txt /pogen/
RUN pip3 install -r /pogen/requirements.txt

# Add devel files
ADD manage.py /pogen/
ADD pogen/ /pogen/pogen
ADD pos/ /pogen/pos

EXPOSE 8080

CMD ["python3","/pogen/manage.py", "runserver", "0.0.0.0:8080"]
