#!/bin/bash

echo "Generating"
mkdir -p prolog_primitives/generatedProto
cd prolog_primitives/generatedProto
python -m grpc_tools.protoc -I ../proto --python_out=. --pyi_out=. --grpc_python_out=. ../proto/*.proto
touch __init__.py
sed -i 's/^\(import.*pb2\)/from . \1/g' *.py
echo "Done"