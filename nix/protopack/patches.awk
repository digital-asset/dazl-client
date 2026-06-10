{
  is_interactive_common = FILENAME ~ /com\/daml\/ledger\/api\/v2\/interactive\/interactive_submission_common_data\.proto$/

  if ($0 ~ /scalapb/) {
    # drop scalapb proto imports and options; scalapb proto files aren't included
    # in the Canton 2 bundle so this causes errors when trying to run codegen, but
    # we don't need them anyway

  } else if (is_interactive_common && $0 ~ /^package .*;$/) {
    # The common data is imported by both the interactive service and its transaction/v1
    # dependency. Give it a leaf Go package to avoid an interactive <-> transaction/v1
    # import cycle.
    print
    print ""
    print "option go_package = \"github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/interactive/common\";"

  } else if (is_interactive_common && $0 ~ /^option go_package = /) {
    # replace the upstream Go package with the leaf package above

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
