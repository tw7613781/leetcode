package leetcode

func twoSum(nums []int, target int) []int {
	cache := make(map[int]int)
	for i, v := range nums {
		w := target - v
		if j, ok := cache[w]; ok {
			return []int{j, i}
		}
		cache[v] = i
	}
	return []int{}
}
