package botw

import "fmt"
import "reflect"
import "github.com/otiai10/twistream"

type IController interface {
	Match(status Status) bool
	Execute(status Status)
}

var controllerRegistry = []IController{}

type Controller struct {
	TL *twistream.Timeline
}

func (c *Controller) Match(status Status) bool {
	return true
}
func (c *Controller) Execute(status Status) {
	// hoge
}

// TODO: hide `twistream` namespace from App
func (c *Controller) Tweet(status Status) error {
	return c.TL.Tweet(status.Status)
}

func AppendController(controller IController) (e error) {
	if _, ok := controller.(IController); !ok {
		return fmt.Errorf("%s does not implement IController", reflect.TypeOf(controller).String())
	}
	controllerRegistry = append(controllerRegistry, controller)
	return
}
