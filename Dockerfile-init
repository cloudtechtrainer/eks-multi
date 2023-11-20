# init-container/Dockerfile
FROM alpine:latest

WORKDIR /app

COPY init-container.sh .

RUN chmod +x init-container.sh

CMD ["./init-container.sh"]
