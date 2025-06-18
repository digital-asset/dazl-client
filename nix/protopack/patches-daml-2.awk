{
  if ($0 ~ /scalapb/) {
    # drop scalapb proto imports and options; scalapb proto files aren't included
    # in the Canton 2 bundle so this causes errors when trying to run codegen, but
    # we don't need them anyway

  } else if ($0 ~ /^package daml_lf_1_16;$/) {
    # Daml-LF 1.17's package name is incorrectly marked as "1.16"
    print "package daml_lf_1_17;"
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_1_17\";"
  
  } else if ($0 ~ /^package daml_lf_1;$/) {
    # move the Daml-LF 1.X Archive wrapper into the same package so that both files
    # can safely be emitted into the same directory
    print "package daml_lf_1_17;"
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_1_17\";"

  } else if ($0 ~ /^package .*;$/) {
    sub(/daml_lf_1_16;$/, "daml_lf_1_17;")

    # write an `option go_package` line based on the contents of the protobuf package
    print

    sub(/^package /, "")
    sub(/;$/, "")
    gsub(/\./, "/")
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/" $0 "\";"

  } else if ($0 ~ /daml_lf_1\.Package daml_lf_1 = 2;/) {
    # because we moved the Daml-LF 1.X Archive wrapper, also drop the import reference
    sub(/daml_lf_1\./, "")
    print

  } else {
    print
  }
}
