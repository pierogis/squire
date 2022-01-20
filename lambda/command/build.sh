pip install ../.. -t package --no-deps

cd package ; zip -r ../../dist/command.zip . -x '*.pyc' ; cd ..
rm -rf package

zip ../dist/command.zip ./handler.py
