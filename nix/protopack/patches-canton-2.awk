{
  if ($0 ~ /scalapb/) {
    # drop scalapb proto imports and options; scalapb proto files aren't included
    # in the Canton 2 bundle so this causes errors when trying to run codegen, but
    # we don't need them anyway

  } else if ($0 ~ /^package .*;$/) {
    # write an `option go_package` line based on the contents of the protobuf package
    print

    sub(/^package /, "")
    sub(/;$/, "")
    gsub(/\./, "/")
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/" $0 "\";"

  } else if ($0 ~ /None = /) {
    # the gRPC Python code generator spits out invalid Python
    # code when fields are called None, so rename fields that
    # we encounter that are called None
    sub(/None/, "None_")
    print

  } else if ($0 ~ /^import "com\/digitalasset\/canton\/time\/admin\/v0\/domain_time_service\.proto";$/) {
    print "import \"com/digitalasset/canton/domain/api/v0/domain_time_service.proto\";"

  } else if ($0 ~ /^import "com\/digitalasset\/canton\/topology\/admin\/v0\/topology_ext\.proto";$/ ) {
    print "import \"com/digitalasset/canton/protocol/v0/topology_ext.proto\";"

  } else {
    print
  }
}
