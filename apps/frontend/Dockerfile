FROM nginx:alpine

RUN mkdir /etc/nginx/ssl/

COPY ./nginx-ssl/certs/mysite.local+3.pem /etc/nginx/ssl/cert.pem
COPY ./nginx-ssl/certs/mysite.local+3-key.pem  /etc/nginx/ssl/key.pem

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

