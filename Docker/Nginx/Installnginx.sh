docker pull nginx

docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx

docker run --name some-nginx -d some-content-nginx

docker run --name some-nginx -d -p 8080:80 some-content-nginx


#! configuration completa 
docker run --name my-custom-nginx-container -v /host/path/nginx.conf:/etc/nginx/nginx.conf:ro -d nginx

docker run --name tmp-nginx-container -d nginx
docker cp tmp-nginx-container:/etc/nginx/nginx.conf /host/path/nginx.conf
docker rm -f tmp-nginx-container