package golangleetcode

import (
	"testing"
)

func TestIsValidSudoku(t *testing.T) {
	var input [][]byte
	inputRow := []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	inputRow = []byte("53..7....")
	input = append(input, inputRow)
	res := isValidSudoku(input)
	if res == true {
		t.Error("should be false")
	}
}
