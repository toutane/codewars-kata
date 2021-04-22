// Vowel Count counts the number of vowels encoutered in a string
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	sen := os.Args[1:][0]
	fmt.Println(GetCount(sen))
}

// GetCount counts vowels in string
func GetCount(str string) int {
	var res int
	arr := strings.Split(str, "")
	for i := 0; i < len(str); i++ {
		switch arr[i] {
		case "a":
			res++
		case "e":
			res++
		case "i":
			res++
		case "o":
			res++
		case "u":
			res++
		}
	}
	return res
}
