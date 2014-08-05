package botw

import "github.com/otiai10/twistream"

type IController interface {
	Match(status twistream.Status) bool
	Execute(status twistream.Status)
}

var controllerRegistry = []IController{}

type Controller struct {
	TL *twistream.Timeline
}

func (c *Controller) Match(status twistream.Status) bool {
	return true
}
func (c *Controller) Execute(status twistream.Status) {
	// hoge
}

// TODO: hide `twistream` namespace from App
func (c *Controller) Tweet(status twistream.Status) error {
	return c.TL.Tweet(status)
}

func AppendController(controller IController) (e error) {
	controllerRegistry = append(controllerRegistry, controller)
	return
}