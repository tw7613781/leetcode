package golangleetcode

import "testing"

func TestReverse(t *testing.T) {
	var input int
	var output int
	var res int
	input = 123
	res = reverse(input)
	output = 321
	if res != output {
		t.Error("the func result should equal to output")
	}
	input = -123
	res = reverse(input)
	output = -321
	if res != output {
		t.Error("the func result should equal to output")
	}
	input = 120
	res = reverse(input)
	output = 21
	if res != output {
		t.Error("the func result should equal to output")
	}
}
