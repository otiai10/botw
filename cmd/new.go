package botw

import "fmt"

type CommandNew struct{}

func (cNew CommandNew) Execute() {
	fmt.Println("Newする")
}
