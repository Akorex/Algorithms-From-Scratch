package main

import "fmt"

func containsDuplicate(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] == nums[j] {
				return true
			}
		}
	}

	return false

}

func main() {

	nums := []int{1, 2, 4, 1}

	fmt.Println(containsDuplicate(nums))
}
