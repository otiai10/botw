package main

import "fmt"
import "os/exec"

type CommandNew struct{}

// {hisyotan}は仮
func (cNew CommandNew) Execute() {
	// skeltonの内容を{src/hisyotan}にコピーする
	cmd := exec.Command("cp", "-R",
		// src pathとか取得せなあかんね
		"/Users/otiai10/proj/go/src/github.com/otiai10/botw/skelton",
		"/Users/otiai10/proj/go/src/hisyotan",
	)
	e := cmd.Run()
	if e != nil {
		fmt.Println(e)
		return
	}
	fmt.Println("App created")
}
