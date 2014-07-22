package controllers

import "fmt"
import "github.com/otiai10/twistream"

type Sample struct{}

func (s *Sample) Match(status twistream.Status) bool {
	return true
}

func (s *Sample) Execute(status twistream.Status) {
	fmt.Println("XXXXXXXXXXXXXXXXXXXX")
}
