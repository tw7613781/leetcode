package golangleetcode

import (
	"strconv"
)

func reverse(x int) int {
	if x < -(2<<31) || x > (2<<31-1) {
		return 0
	}
	xStr := strconv.Itoa(x)
	xByte := []byte(xStr)
	if xByte[0] == 45 {
		res := reverseString(xByte[1:])
		resStr := string(res)
		resInt, _ := strconv.Atoi(resStr)
		return -resInt
	}
	res := reverseString(xByte)
	resStr := string(res)
	resInt, _ := strconv.Atoi(resStr)
	return resInt
}

func reverseString(s []byte) []byte {
	length := len(s)
	for i := 0; i < length/2; i++ {
		s[i], s[length-1-i] = s[length-1-i], s[i]
	}
	i := 0
	for i < length {
		if s[i] != 48 {
			break
		}
		i++
	}
	return s[i:]
}
