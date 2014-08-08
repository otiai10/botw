package events

import "github.com/otiai10/botw"

type OnError struct {
	*botw.Action
}

func (oe *OnError) Execute(e error) {
	println(e.Error())
}
