package main

import (
	"fmt"

	kata7 "github.com/toutane/codewars-kata/go/7kyu"
	kata8 "github.com/toutane/codewars-kata/go/8kyu"
)

func main() {
	kata8.MakeUpperCase("hello, world")
	// Expected: "HELLO, WORLD"

	x := []float64{0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25}
	kata7.Gps(15, x)
	// Expected: 74 (max speed "floor")

	str := "ZpglnRxqenU"
	kata7.Accum(str)
	// Expected: "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"

	fmt.Println(kata7.Solution("abc", "bc"))
	// Expected: true
}
