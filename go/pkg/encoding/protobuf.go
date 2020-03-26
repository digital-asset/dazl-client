package encoding

import v1 "github.com/digital-asset/dazl/go/gen/com/daml/ledger/api/v1"

func ConvertRecordToNative(record *v1.Record) map[string]interface{} {
	m := make(map[string]interface{})
	for _, field := range record.Fields {
		m[field.Label] = ValueToNative(field.Value)
	}
	return m
}

func VariantToNative(variant *v1.Variant) map[string]interface{} {
	return map[string]interface{}{
		"tag":   variant.Constructor,
		"value": ValueToNative(variant.Value),
	}
}

func ContractIdToNative(cid string) string {
	return cid
}

func ListToNative(list *v1.List) []interface{} {
	l := make([]interface{}, len(list.Elements))
	for i, elem := range list.Elements {
		l[i] = ValueToNative(elem)
	}
	return l
}

func Int64ToNative(i int64) int64 {
	return i
}

func ValueToNative(value *v1.Value) interface{} {
	switch value.Sum.(type) {
	case *v1.Value_Record:
		return ConvertRecordToNative(value.GetRecord())
	case *v1.Value_Variant:
		return VariantToNative(value.GetVariant())
	case *v1.Value_ContractId:
		return ContractIdToNative(value.GetContractId())
	case *v1.Value_List:
		return ListToNative(value.GetList())
	case *v1.Value_Int64:
		return Int64ToNative(value.GetInt64())
	case *v1.Value_Numeric:
		return NumericToNative(value.GetNumeric())
	case *v1.Value_Text:
		return TextToNative(value.GetText())
	case *v1.Value_Timestamp:
		return TimestampToNative(value.GetTimestamp())
	case *v1.Value_Party:
		return PartyToNative(value.GetParty())
	case *v1.Value_Bool:
		return BoolToNative(value.GetBool())
	case *v1.Value_Unit:
		return UnitToNative(value.GetUnit())
	case *v1.Value_Date:
		return DateToNative(value.GetDate())
	case *v1.Value_Optional:
		return OptionalToNative(value.GetOptional())
	case *v1.Value_Map:
		return TextMapToNative(value.GetMap())
	case *v1.Value_Enum:
		return EnumToNative(value.GetMap())
	case *v1.Value_GenMap:
		return GenMapToNative(value.GetGenMap())
	}
}

type TypeProvider interface {
}

type ValueConverter interface {
	ConvertRecord(typeProvider *TypeProvider, record *v1.Record) (interface{}, error)
	ConvertVariant(typeProvider *TypeProvider, variant *v1.Record) (interface{}, error)
	ConvertContractId(typeProvider *TypeProvider, contractId string) (interface{}, error)
	ConvertList(typeProvider *TypeProvider)
}

type nativeTypeConverter struct{}

func (tc nativeTypeConverter) ConvertRecord(record *v1.Record) interface{} {
	return ConvertRecordToNative(record)
}
