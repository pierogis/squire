all: layers lambda

.PHONY: layers
layers:
	rm -rf layers/dist
	docker run \
	  --rm -it \
	  --name squire-build-layers \
	  --mount type=bind,source=$(PWD)/layers,target=/var/task/layers \
	  "public.ecr.aws/sam/build-python3.9" \
	  /bin/sh -c "cd layers; . ./layers.sh"


.PHONY: lambda
lambda:
	rm -rf dist
	docker run \
	  --rm -it \
	  --name squire-build-lambda \
	  --mount type=bind,source=$(PWD),target=/var/task/lambda \
	  --mount type=bind,source=$(PWD)/../squire,target=/var/task/squire,readonly \
	  --mount type=bind,source=$(PWD)/../pyproject.toml,target=/var/task/pyproject.toml,readonly \
	  "public.ecr.aws/sam/build-python3.9" \
	  /bin/sh -c "cd lambda; . ./build.sh"


.PHONY: slash
slash:
	python -m slash


.PHONY: clean
clean:
	rm -rf dist
	rm -rf layers/dist