package main

import (
	"fmt"
	"github.com/toutane/codewars-kata/go/8kyu"
	"github.com/toutane/codewars-kata/go/7kyu"
)

func main() {
	fmt.Println(kata8.MakeUpperCase("hello, world"))
	// Expected : "HELLO, WORLD"

	x := []float64{0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25}
	fmt.Println(kata7.Gps(15, x))
	// Expected : 74 (max speed "floor")
}
