package main

func productExceptSelf(nums []int) []int {
	ans := make([]int, len(nums))

	prefix := 1
	for i := 0; i < len(nums); i++ {
		ans[i] = prefix
		prefix *= nums[i]
	}

	suffix := 1
	for j := len(nums) - 1; j >= 0; j-- {
		ans[j] *= suffix
		suffix *= nums[j]

	}

	return ans
}
