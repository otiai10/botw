package main

import "fmt"
import "bufio"
import "os"
import "os/exec"
import "go/build"
import "path/filepath"
import "github.com/otiai10/flagg"

type CommandNew struct{}

// {hisyotan}は仮
func (cNew CommandNew) Execute() {
	gopath := build.Default.GOPATH
	appName := flagg.Arg(1)
	appPath := filepath.Join(
		gopath, "src",
		filepath.Join(filepath.Split(appName)),
	)
	if *flagg.Bool("force", false, "Remove existing directory") {
		reader := bufio.NewReader(os.Stdin)
		fmt.Printf("Destroy and Create new `%s`? (YES/n): ", appPath)
		if text, _ := reader.ReadString('\n'); text == "YES\n" {
			exec.Command("rm", "-rf", appPath).Run()
		}
	}
	if pkg, e := build.Import(appName, "", build.FindOnly); e == nil {
		fmt.Println("Directory already exists at ", pkg.Dir)
		return
	}
	skelPath := filepath.Join(gopath, "src", "github.com/otiai10/botw", "skelton")
	cmd := exec.Command("cp", "-R", skelPath, appPath)
	cmd.Stderr = os.Stderr
	e := cmd.Run()
	if e != nil {
		fmt.Println("`botw new` failed: ", e)
		return
	}
	fmt.Println("New bot created at ", appPath)
}
