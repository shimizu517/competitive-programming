// TLE
package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	MaxTextSizee = 1000000
)

func rabinKarp(p, t string, d, q int) {
	m, n, h := len(p), len(t), 1
	if n < m {
		return
	}
	var ph, th int
	for i := 0; i < m-1; i++ {
		h = (h * d)
	}
	for i := 0; i < m; i++ {
		ph = (d*ph + int(p[i]))
		th = (d*th + int(t[i]))
	}
	wr := bufio.NewWriter(os.Stdout)

	for i := 0; i < n-m+1; i++ {
		// if true, p and t[i:i+m] can be the same.
		if ph == th {
			//fmt.Println(i)
			wr.WriteString(strconv.Itoa(i) + "\n")
		}

		if i < n-m {
			// calculate hash for next window of t.
			th = (d*(th-int(t[i])*h) + int(t[i+m]))
			if th < 0 {
				th = th + q
			}
		}
	}
	wr.Flush()
}

func main() {
	var s *bufio.Scanner = bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanWords)
	buffer := make([]byte, MaxTextSizee+1)
	s.Buffer(buffer, MaxTextSizee+1)
	var t, p string
	if s.Scan() {
		t = s.Text()
	}
	if s.Scan() {
		p = s.Text()
	}
	rabinKarp(p, t, 256, 101)
}
