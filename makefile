build-image:
	docker build -t many-cves .

run-image-docker:
	docker rm --force many-cves || true
	docker run -d --name many-cves --rm many-cves 
	docker logs --follow many-cves

stop-image:
	docker stop many-cves

push-image:
	docker tag many-cves:latest ghcr.io/ccollicutt/many-cves:latest
	docker push ghcr.io/ccollicutt/many-cves:latest

run-image-kubernetes:
	kubectl create -f kubernetes/deployment.yaml


