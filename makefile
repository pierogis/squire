.PHONY: build
build:
	rm -rf .venv
	sam build --use-container --cached

.PHONY: build-NumpyLayer
build-NumpyLayer:
	pip install -r layers/numpy/requirements.txt -t $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-PandasLayer
build-PandasLayer:
	pip install -r layers/pandas/requirements.txt -t $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-OpenaiLayer
build-OpenaiLayer:
	pip install -r layers/openai/requirements.txt -t $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-PynaclLayer
build-PynaclLayer:
	pip install -r layers/pynacl/requirements.txt -t $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-CommandFunction
build-CommandFunction:
	pip install . -t $(ARTIFACTS_DIR) --no-deps
	cp command/handler.py $(ARTIFACTS_DIR)/handler.py

.PHONY: build-InteractionFunction
build-InteractionFunction:
	cp interaction/handler.py $(ARTIFACTS_DIR)/handler.py
