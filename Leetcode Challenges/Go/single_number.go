package main

func singleNumber(nums []int) int {
	seen := make(map[int]int)

	for _, num := range nums {
		seen[num]++
	}

	for num, count := range seen {
		if count == 1 {
			return num
		}
	}

	return 0
}
