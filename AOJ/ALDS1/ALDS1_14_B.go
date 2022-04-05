package main

import (
	"bufio"
	"fmt"
	"os"
)

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
	sizeP := len(p)

	for i := 0; i < len(t)-sizeP+1; i++ {
		if p == t[i:(i+sizeP)] {
			fmt.Println(i)
		}
	}
}
