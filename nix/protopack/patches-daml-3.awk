{
  if ($0 ~ /scalapb/) {
    # drop scalapb proto imports and options; scalapb proto files aren't included
    # in the Canton 2 bundle so this causes errors when trying to run codegen, but
    # we don't need them anyway

  } else if ($0 ~ /^package daml_lf_2_1;$/) {
    # write a go package that is consistent with the location of the protobuf file
    print
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1\";"
  
  } else if ($0 ~ /^package daml_lf_2;$/) {
    # move the Daml-LF 2.X Archive wrapper into the same package so that both files
    # can safely be emitted into the same directory
    print "package daml_lf_2_1;"
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1\";"

  } else if ($0 ~ /^package .*;$/) {
    # write an `option go_package` line based on the contents of the protobuf package
    print

    sub(/^package /, "")
    sub(/;$/, "")
    gsub(/\./, "/")
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/" $0 "\";"

  } else if ($0 ~ /daml_lf_2\.Package daml_lf_2 = 4;/) {
    # because we moved the Daml-LF 2.X Archive wrapper, also drop the import reference
    sub(/daml_lf_2\./, "")
    print

  } else {
    print
  }
}
