run:
	docker build . -t seqserv-with-customisations --target=minify

dls:
	docker container ls

remove:
	docker stop $(id)
	docker rm $(id)
