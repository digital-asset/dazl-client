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

  } else {
    print
  }
}
