package main

import (
	"bufio"
	"fmt"
	"os"
)

// not optimized. you should use q for hashing method.
func rabinKarp(p, t string, d, q int) {
	m, n, h := len(p), len(t), 1
	if n < m {
		return
	}
	var ph, th int
	for i := 0; i < m-1; i++ {
		h = h * d
	}
	for i := 0; i < m; i++ {
		ph = d*ph + int(p[i])
		th = d*th + int(t[i])
	}

	for i := 0; i < n-m+1; i++ {
		// if true, p and t[i:i+m] can be the same.
		if ph == th {
			var j = 0
			for ; j < m; j++ {
				if t[i+j] != p[j] {
					break
				}
			}
			if j == m {
				fmt.Println(i)
			}
		}

		if i < n-m {
			// calculate hash for next window of t.
			th = d*(th-int(t[i])*h) + int(t[i+m])
		}
	}
}

func main() {
	var s *bufio.Scanner = bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanWords)
	var t, p string
	if s.Scan() {
		t = s.Text()
	}
	if s.Scan() {
		p = s.Text()
	}
	rabinKarp(p, t, 256, 101)
}
