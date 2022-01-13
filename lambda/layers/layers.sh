pip install pynacl --target python
zip -r dist/pynacl.zip python
rm -rf python

pip install numpy --target python
zip -r dist/numpy.zip python
rm -rf python

pip install pandas pytz six --target python --no-deps
zip -r dist/pandas.zip python
rm -rf python