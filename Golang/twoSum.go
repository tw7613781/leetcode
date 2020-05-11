package leetcode

import "sort"

func search(nums []int, target int) int {
	index := sort.SearchInts(nums, target)
	if nums[index] == target {
		return index
	}
	return -1
}

func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums)-1; i++ {
		k := search(nums[i+1:], target-nums[i])
		if k != -1 {
			return []int{i, k}
		}
	}
	return []int{0, 0}
}
