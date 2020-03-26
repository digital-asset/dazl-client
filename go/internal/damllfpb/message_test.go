package damllfpb

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRenderGoModel(t *testing.T) {
	_, err := BuildRoot()
	if err != nil {
		t.Fatal(err)
	}
}


func TestGoName(t *testing.T) {
	actual := goName("Type.Con", true)
	assert.Equal(t, "TypeCon", actual)
}