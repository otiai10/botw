package controllers

import "fmt"

// import "github.com/otiai10/twistream" //これいやだなー
import "github.com/otiai10/botw"

type Sample struct {
	*botw.Controller
}

func (s *Sample) Match(status botw.Status) bool {
	return true
}

func (s *Sample) Execute(status botw.Status) {
	fmt.Printf("------------------ IN SAMPLE -------------------\n%+v\n", status)
}
