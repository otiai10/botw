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
	}
}
