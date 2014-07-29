package botw

import "github.com/otiai10/twistream"

type IController interface {
	Match(status twistream.Status) bool
	Execute(status twistream.Status)
}

var controllerRegistry = []IController{}

func AppendController(controller IController) (e error) {
	controllerRegistry = append(controllerRegistry, controller)
	return
}
