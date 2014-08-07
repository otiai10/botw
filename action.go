package botw

import "fmt"
import "reflect"
import "github.com/otiai10/twistream"

type IAction interface {
	Match(status Status) bool
	Execute(status Status)
}

var actionRegistry = []IAction{}

type Action struct {
	TL *twistream.Timeline
}

func (c *Action) Match(status Status) bool {
	return true
}
func (c *Action) Execute(status Status) {
	// hoge
}

// TODO: hide `twistream` namespace from App
func (c *Action) Tweet(status Status) error {
	return c.TL.Tweet(status.Status)
}

func AppendAction(action IAction) (e error) {
	if _, ok := action.(IAction); !ok {
		return fmt.Errorf("%s does not implement IAction", reflect.TypeOf(action).String())
	}
	actionRegistry = append(actionRegistry, action)
	return
}
