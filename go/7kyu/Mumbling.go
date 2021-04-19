package kata7

import "strings"

func Accum(s string) string {
	str := strings.ToUpper(s)
	arr := strings.Split(str, "")
	res := arr[0]
	for i := 1; i < len(s); i++ {
		same := strings.Repeat(strings.ToLower(arr[i]), i)
		part := arr[i] + same
		res = res + "-" + part
	}
	return res
}
