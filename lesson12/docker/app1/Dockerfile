FROM ubuntu:20.04
RUN apt update && apt -y install cowsay fortune
RUN mkdir /app
ADD ./run.sh /app/
WORKDIR /app/

ENTRYPOINT ["/app/run.sh"]
