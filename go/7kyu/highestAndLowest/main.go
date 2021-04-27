// Highest And Lowest take a list of number in a string and return the highest
// and the lowest also in a string
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(HighAndLow("8 5 -1"))
}

func HighAndLow(str string) string {
	var narr []int
	arr := strings.Split(str, " ")
	for i := 0; i < len(arr); i++ {
		n, _ := strconv.Atoi(arr[i])
		narr = append(narr, n)
	}
	var max, min = narr[0], narr[0]
	for i := 0; i < len(narr); i++ {
		if narr[i] >= max {
			max = narr[i]
		} else if narr[i] <= min {
			min = narr[i]
		}
	}
	return fmt.Sprintf("%d %d", max, min)
}
