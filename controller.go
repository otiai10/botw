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
func (c *Controller) Some() string {
	c.TL.Tweet(twistream.Status{
		Text: "@otiai10 いぇっす",
	})
	return "This is Base.Some"
}

func AppendController(controller IController) (e error) {
	controllerRegistry = append(controllerRegistry, controller)
	return
}
