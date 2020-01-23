FROM python:2.7.17-slim-buster

COPY . /tests
RUN apt-get update
RUN apt-get -y install gnupg
RUN apt-get -y install wget
RUN apt-get -y install curl

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install python packages
RUN pip install -r /tests/requirements.txt
# Run test on container start
CMD pytest /tests/ --capture=no
