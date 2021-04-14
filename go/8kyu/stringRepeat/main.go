package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	args := os.Args[1:]
	rep, _ := strconv.Atoi(args[0])
	str := args[1]
	fmt.Println(RepeatStr(rep, str))

}

func RepeatStr(repetitions int, value string) string {
	var result string
	for i := 0; i < repetitions; i++ {
		result += value
	}
	return result
}
