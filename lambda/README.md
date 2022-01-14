# lambda

You can run this package as an aws lambda function
that will receive events from discord via http

`make` will build requisite lambda layers and function
package inside a docker container

Upload the artifacts in `dist` to lambda function
and `layers/dist` to 4 lambda layers

The function should use the layers in the following
order:
 1. numpy
 2. pandas
 3. openai
 4. pynacl