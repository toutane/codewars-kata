// Factorial function https://wikipedia.org/wiki/Factorial
package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	n, _ := strconv.Atoi(os.Args[1:][0])
	fmt.Println(Factorial(n))
}

func Factorial(n int) int {
	var res int = 1
	for i := 1; i <= n; i++ {
		res *= i
	}
	return res
}
