{
  if ($0 ~ /scalapb/) {
    # drop scalapb proto imports and options; scalapb proto files aren't included
    # in the Canton 2 bundle so this causes errors when trying to run codegen, but
    # we don't need them anyway

  } else if ($0 ~ /^package daml_lf_2_1;$/) {
    # (legacy 3.3.x) write a go package that is consistent with the location of the protobuf file
    print
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1\";"

  } else if ($0 ~ /^package daml_lf;$/) {
    # (3.4.9+) daml_lf wrapper - rename to daml_lf_2_1 and keep original path
    print "package daml_lf_2_1;"
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1\";"

  } else if ($0 ~ /^package daml_lf_2;$/) {
    # (3.4.9+) daml_lf_2 - rename to daml_lf_2_1 and merge into same package
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
