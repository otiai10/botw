package botw

import "github.com/otiai10/twistream"

type Status struct {
	twistream.Status
}

func NewStatus(text string, options map[string]string) Status {
	status := Status{}
	status.Text = text
	return status
}
