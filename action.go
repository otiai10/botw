package botw

import "fmt"
import "reflect"
import "github.com/otiai10/twistream"

// MatchExecuter ...
type MatchExecuter interface {
	Match(status Status) bool
	Execute(status Status)
}

var actionRegistry = []MatchExecuter{}

// Action ...
type Action struct {
	TL *twistream.Timeline
}

// Match ...
func (c *Action) Match(status Status) bool {
	return true
}

// Execute ...
func (c *Action) Execute(status Status) {
	// hoge
}

// Tweet ...
func (c *Action) Tweet(status Status) error {
	return c.TL.Tweet(status.Status)
}

// AppendAction ...
func AppendAction(action MatchExecuter) (e error) {
	if _, ok := action.(MatchExecuter); !ok {
		return fmt.Errorf("%s does not implement MatchExecutor", reflect.TypeOf(action).String())
	}
	actionRegistry = append(actionRegistry, action)
	return
}
