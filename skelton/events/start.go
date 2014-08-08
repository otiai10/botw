package events

import "github.com/otiai10/botw"
import "time"

type OnStart struct {
	*botw.Action
}

func (act *OnStart) Execute() {
	status := botw.NewStatus(
		time.Now().String()+", 起動しましたー",
		map[string]string{},
	)
    act.Tweet(status)
}
