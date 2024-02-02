Image=tbutzer/sphinx
html:
	rm -fr ./build
	docker run\
           -v `pwd`:/home \
           ${Image} sphinx-build source build/html
	cp -r build/html/* ../docs

webServer:
	docker run --name harmony-web -p 80:80 -v `pwd`/build/html:/usr/share/nginx/html:ro -d nginx

joseWeb:
	docker run --rm --name harmony-web -p 7778:80 -v `pwd`/build/html:/usr/share/nginx/html:ro -d nginx


git:
	#(cd /iarpa/opt/butzer/opt/bslurm2 && make publish)
	(cd ~/opt/bslurm2 && make publish)


all: html git
