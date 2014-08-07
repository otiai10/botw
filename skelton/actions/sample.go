package actions

import "fmt"
import "github.com/otiai10/botw"

type Sample struct {
	*botw.Action
}

// See https://godoc.org/github.com/otiai10/twistream#Status to know Statsu structure
func (s *Sample) Match(status botw.Status) bool {
	return true
}

func (s *Sample) Execute(status botw.Status) {
	fmt.Printf("------------------ IN SAMPLE -------------------\n%+v\n", status)
}
