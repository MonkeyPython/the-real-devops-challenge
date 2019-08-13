FROM ubuntu

RUN mkdir -p /opt/app/src

COPY docker-entrypoint.sh /
COPY ../../requirements.txt /opt/app/requirements.txt
COPY ../../src/* /opt/app/src/
COPY ../../app.py /opt/app/

RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install \
    python3 \
    python3-pip

RUN pip3 install -r /opt/app/requirements.txt
RUN chmod +x /docker-entrypoint.sh /opt/app/app.py

EXPOSE 8080

ENV MONGO_URI=mongodb://172.17.0.3:27017/servicesDB

ENTRYPOINT ["./docker-entrypoint.sh"]
