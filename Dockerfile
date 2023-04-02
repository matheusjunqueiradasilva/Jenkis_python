FROM jenkins/jenkins

WORKDIR /JENKINS_PYTHON

USER root

COPY -- python ./
 
RUN apt update

RUN apt upgrade -y

RUN apt install python3-pip -y

RUN apt install python3 -y

RUN pip3 install -r requirements.txt

RUN apt install git -y
   

