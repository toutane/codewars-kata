package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	args := os.Args[1:]
	//k, _ := strconv.Atoi(args[0])
	start, _ := strconv.Atoi(args[1])
	nd, _ := strconv.Atoi(args[2])
	interv := nd - start
	var res []int
	ch := make(chan int)
	for i := start; i < nd; i++ {
		go IsPrime(i, ch)
	}
	for i := 0; i < interv; i++ {
		res = append(res, <-ch)
		fmt.Println(<-ch)
	}
	fmt.Println(res)
}

func IsPrime(n int, ch chan<- int) {
	ch <- n % 2
}
