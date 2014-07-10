package hisyotan

import "fmt"

type CommandHelp struct {}

func (cHelp CommandHelp) Execute() {
    fmt.Println("This is help")
}
