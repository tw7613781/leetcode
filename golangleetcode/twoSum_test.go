package golangleetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTwoSum(t *testing.T) {
	/*****case 1*****/
	nums := []int{2, 7, 11, 15}
	target := 9
	res := twoSum(nums, target)
	assert.Equal(t, []int{0, 1}, res, "")
	/*****case 2*****/
	nums1 := []int{0, 1, 5, 10}
	target1 := 11
	res1 := twoSum(nums1, target1)
	assert.Equal(t, []int{1, 3}, res1, "")
}
