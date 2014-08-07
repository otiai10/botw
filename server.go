package botw

import (
	"github.com/otiai10/twistream"
)

var (
	CONSUMERKEY       = ""
	CONSUMERSECRET    = ""
	ACCESSTOKEN       = ""
	ACCESSTOKENSECRET = ""
)

func InitVars(ck, cs, at, as string) (e error) {
	CONSUMERKEY = ck
	CONSUMERSECRET = cs
	ACCESSTOKEN = at
	ACCESSTOKENSECRET = as
	return
}

func Serve(tl *twistream.Timeline) chan error {

	terminator := make(chan error)

	go func(terminator chan error) {
		for {
			_status := <-tl.Listen()
			status := Status{_status}
			for _, action := range actionRegistry {
				if action.Match(status) {
					action.Execute(status)
					break
				}
			}
		}
	}(terminator)

	return terminator
}
