mkdir -p dist

pip install -r pynacl/requirements.txt --target python --no-deps
zip -r dist/pynacl.zip python
rm -rf python

pip install -r numpy/requirements.txt --target python --no-deps
zip -r dist/numpy.zip python
rm -rf python

pip install -r pandas/requirements.txt --target python --no-deps
zip -r dist/pandas.zip python
rm -rf python

pip install -r openai/requirements.txt --target python --no-deps
zip -r dist/openai.zip python
rm -rf python
