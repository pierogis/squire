.PHONY: build-NumpyLayer
build-NumpyLayer:
	pip install -r $(PWD)/layers/numpy/requirements.txt --target $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-PandasLayer
build-PandasLayer:
	pip install -r $(PWD)/layers/pandas/requirements.txt --target $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-OpenaiLayer
build-OpenaiLayer:
	pip install -r $(PWD)/layers/openai/requirements.txt --target $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-PynaclLayer
build-PynaclLayer:
	pip install -r $(PWD)/layers/pynacl/requirements.txt --target $(ARTIFACTS_DIR)/python --no-deps

.PHONY: build-CommandFunction
build-CommandFunction:
	pip install $(PWD)/.. -t $(ARTIFACTS_DIR) --no-deps
	cp $(PWD)/command/handler.py $(ARTIFACTS_DIR)/handler.py

.PHONY: build-InteractionFunction
build-InteractionFunction:
	cp $(PWD)/interaction/handler.py $(ARTIFACTS_DIR)/handler.py
