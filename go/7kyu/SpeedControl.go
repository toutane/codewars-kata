package kata7

import "math"

func Gps(s int, x []float64) int {

	v := make([]int, 0)

	for i:=0; i < (len(x)-1); i++ {
		k := int(3600 * math.Abs(x[i] - x[i + 1])) / s
		v = append(v , k)
	}

	max := 0
	for z:=0; z < len(v); z++ {
		if v[z] > max {
			max = v[z]
		}
	}
	return max
}
