package main

import (
	"fmt"
	"github.com/otiai10/botw"
	"github.com/otiai10/flagg"
	"go/build"
	"go/parser"
	"go/token"
	"os"
	"os/exec"
	"path/filepath"
	"text/template"
)

type Command interface {
	Execute()
}

type CommandRun struct{}

// うおーめんどくせー
type writer struct{}

var pool = []byte{}

func (w writer) Write(b []byte) (n int, e error) {
	pool = append(pool, b...)
	return
}

type templatingParams struct {
	AppName string
	Actions []string
}

func (cRun CommandRun) Execute() {

	// TODO: DRY
	gopath := build.Default.GOPATH
	appName := flagg.Arg(1)

	appPath := filepath.Join(gopath, "src", appName)
	// コントローラ名を取得する
	pkgs, _ := parser.ParseDir(token.NewFileSet(), filepath.Join(appPath, "actions"), func(f os.FileInfo) bool {
		// とりあえずぜんぶtrue
		return true
	}, 0)
	params := templatingParams{
		AppName: appName,
		Actions: botw.GetAllActionNames(pkgs["actions"]),
	}
	tpl, _ := template.New("tmp/main").Parse(MAIN)
	tpl.Execute(writer{}, params)

	// ここでmain.mainのソースコードが完成したので、tmp/mainに書き込む
	// 今あるものを消す
	tmpMainPath := filepath.Join(appPath, "tmp", "main.go")
	_ = os.Remove(tmpMainPath)
	// 新しくつくる
	_ = os.Mkdir(filepath.Join(appPath, "tmp"), 0755) // TODO: DRY
	f, _ := os.Create(tmpMainPath)
	f.Write(pool)

	// binをビルドする
	// go build -o /Users/otiai10/proj/go/bin/hisyotan hisyotan/tmp
	cmd := exec.Command("go", "build",
		// hoge/fugaでnewされたものはこれSplitして末尾とるひつようある
		"-o", filepath.Join(gopath, "bin", appName),
		filepath.Join(appName, "tmp"),
	)
	if e := cmd.Run(); e != nil {
		fmt.Println("build failed: ", e)
		return
	}

	// appを実行する
	pkg, _ := build.Default.Import(appName, "", build.FindOnly)

	binPath := filepath.Join(pkg.BinDir, appName)
	cmd = exec.Command(binPath)
	// 出力をこっちにする
	cmd.Stdout, cmd.Stderr = os.Stdout, os.Stderr
	if e := cmd.Run(); e != nil {
		fmt.Println("App start failed: ", e)
		return
	}
	fmt.Println("App started")

	// なんかあるまではこっちのプロセスで監視してる
	finisher := make(chan bool)
	go func() {
		select {
		case <-finisher:
			cmd.Process.Kill()
			fmt.Println("App Ended")
			os.Exit(1)
			return
		}
	}()
}

const MAIN = `// AUTO GENERATED MAIN PROCESS
// DO NOT EDIT
package main

import "github.com/otiai10/botw"
import "github.com/otiai10/twistream"

import "{{.AppName}}/actions"
import "{{.AppName}}/events"
import "{{.AppName}}/conf"

func main() {
	botw.InitVars(
		conf.CONSUMERKEY,
		conf.CONSUMERSECRET,
		conf.ACCESSTOKEN,
		conf.ACCESSTOKENSECRET,
	)
    timeline, _ := twistream.New(
        "https://userstream.twitter.com/1.1/user.json",
		conf.CONSUMERKEY,
		conf.CONSUMERSECRET,
		conf.ACCESSTOKEN,
		conf.ACCESSTOKENSECRET,
    )
    a := &botw.Action{
        TL: timeline,
    }

	{{range .Actions}}
	botw.AppendAction(&actions.{{.}}{a})
	{{end}}

    onStart := &events.OnStart{a}
    onStart.Execute()

    onError := &events.OnError{a}
	e := <- botw.Serve(timeline)
    onError.Execute(e)
    panic(e.Error())
}
`
