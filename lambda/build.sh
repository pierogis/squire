pip install -r requirements.txt --no-deps -t dist/package
pip install .. -t dist/package --no-deps

cd dist/package ; zip -r ../lambda.zip . -x '*.pyc' ; cd ../..
rm -rf dist/package

zip dist/lambda.zip ./handler.py
