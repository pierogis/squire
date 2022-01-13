pip wheel . --no-deps --wheel-dir=dist
pip install --upgrade -t package dist/*.whl --no-deps
pip install -t dist/package -r lambda/requirements.txt --no-deps
cd dist/package ; zip -r ../lambda.zip . -x '*.pyc' ; cd ../..
cd lambda ; zip ../dist/lambda.zip ./handler.py
cd .. ; rm -rf dist/package