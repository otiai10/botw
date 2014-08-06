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

func Serve() chan error {

	terminator := make(chan error)

	go func(terminator chan error) {
		timeline, e := twistream.New(
			"https://userstream.twitter.com/1.1/user.json",
			CONSUMERKEY,
			CONSUMERSECRET,
			ACCESSTOKEN,
			ACCESSTOKENSECRET,
		)
		if e != nil {
			terminator <- e
		}
		for {
			_status := <-timeline.Listen()
			status := Status{_status}
			for _, controller := range controllerRegistry {
				if controller.Match(status) {
					controller.Execute(status)
					break
				}
			}
		}
	}(terminator)

	return terminator
}
