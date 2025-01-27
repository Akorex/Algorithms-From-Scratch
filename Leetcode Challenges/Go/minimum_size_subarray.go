package main

func minSubArrayLen(target int, nums []int) int {
	start, sum := 0, 0
	ans := len(nums) + 1

	for end := 0; end < len(nums); end++ {
		sum += nums[end]

		for sum >= target {
			if ans > end-start+1 {
				ans = end - start + 1
			}

			sum -= nums[start]
			start += 1
		}
	}

	if ans == len(nums)+1 {
		return 0
	}

	return ans

}
