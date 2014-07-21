package botw

import "fmt"

type Command interface {
	Execute()
}

type CommandRun struct{}

func (cRun CommandRun) Execute() {
	fmt.Println("This is command run")
}
