import sys
from google.protobuf.compiler import plugin_pb2 as plugin

from grpc_tools import protoc


def generate_code(request: plugin.CodeGeneratorRequest, response):
    print(request)
    protoc.main()


def main():
    # Read request message from stdin
    data = sys.stdin.read()

    # Parse request
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(data)

    # Create response
    response = plugin.CodeGeneratorResponse()

    # Generate code
    generate_code(request, response)

    # Serialise response message
    output = response.SerializeToString()

    # Write to stdout
    sys.stdout.write(output)