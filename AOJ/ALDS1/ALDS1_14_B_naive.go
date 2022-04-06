package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	MAX_TEXT_SIZE = 1000000
)

func main() {
	var s *bufio.Scanner = bufio.NewScanner(os.Stdin)
	s.Split(bufio.ScanWords)
	buffer := make([]byte, MAX_TEXT_SIZE+1)
	s.Buffer(buffer, MAX_TEXT_SIZE+1)
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
