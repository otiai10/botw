package botw

import (
	"fmt"
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

type IController interface {
	Match(status twistream.Status) bool
	Execute(status twistream.Status)
}

var controllerRegistry = []IController{}

func Serve() {
	timeline, _ := twistream.New(
		"https://userstream.twitter.com/1.1/user.json",
		CONSUMERKEY,
		CONSUMERSECRET,
		ACCESSTOKEN,
		ACCESSTOKENSECRET,
	)
	for {
		status := <-timeline.Listen()
		fmt.Printf("%+v\n", status)
		for _, controller := range controllerRegistry {
			if controller.Match(status) {
				controller.Execute(status)
				break
			}
		}
	}
}

func AppendController(controller IController) (e error) {
	controllerRegistry = append(controllerRegistry, controller)
	return
}
