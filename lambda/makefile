all: layers lambdas

.PHONY: layers
layers:
	mkdir -p dist
	docker run \
	  --rm -it \
	  --name squire-build-layers \
	  --mount type=bind,source=$(PWD)/layers,target=/var/task/lambda/layers \
	  --mount type=bind,source=$(PWD)/dist,target=/var/task/lambda/dist \
	  "public.ecr.aws/sam/build-python3.9" \
	  /bin/sh -c "cd lambda/layers; . ./build.sh"


.PHONY: command
command:
	mkdir -p dist
	docker run \
	  --rm -it \
	  --name squire-build-command \
	  --mount type=bind,source=$(PWD)/dist,target=/var/task/lambda/dist \
	  --mount type=bind,source=$(PWD)/command,target=/var/task/lambda/command \
	  --mount type=bind,source=$(PWD)/../squire,target=/var/task/squire,readonly \
	  --mount type=bind,source=$(PWD)/../pyproject.toml,target=/var/task/pyproject.toml,readonly \
	  "public.ecr.aws/sam/build-python3.9" \
	  /bin/sh -c "cd lambda/command; . ./build.sh"

.PHONY: interaction
interaction:
	mkdir -p dist
	docker run \
	  --rm -it \
	  --name squire-build-interaction \
	  --mount type=bind,source=$(PWD)/dist,target=/var/task/lambda/dist \
	  --mount type=bind,source=$(PWD)/interaction,target=/var/task/lambda/interaction,readonly \
	  "public.ecr.aws/sam/build-python3.9" \
	  /bin/sh -c "cd lambda/interaction; . ./build.sh"

lambdas: interaction command

.PHONY: slash
slash:
	python -m slash


.PHONY: clean
clean:
	rm -rf dist