FROM ubuntu as dependency

WORKDIR /JENKINS_PYTHON

COPY -- python ./
 
RUN apt update

RUN apt upgrade -y

RUN apt-get install gnupg2 -y

Run apt-get install wget -y

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5BA31D57EF5975CA

RUN wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -

RUN sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'

RUN apt-get update

RUN apt-get install fontconfig openjdk-11-jre -y

RUN  apt-get install jenkins -y

RUN apt install python3-pip -y

RUN pip3 install -r requirements.txt

RUN apt install git -y
   

