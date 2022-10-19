FROM ubuntu

COPY requirements.txt requirements.txt
RUN apt-get update && \
	apt install -y python3 gcc python3-pip
RUN pip install -r requirements.txt
