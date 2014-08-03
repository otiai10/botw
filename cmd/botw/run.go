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

// 開発用
import (
	"time"
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
	AppName     string
	Controllers []string
}

func (cRun CommandRun) Execute() {

	// TODO: DRY
	gopath := build.Default.GOPATH
	appName := flagg.Arg(1)

	appPath := filepath.Join(gopath, "src", appName)
	// コントローラ名を取得する
	pkgs, _ := parser.ParseDir(token.NewFileSet(), filepath.Join(appPath, "controllers"), func(f os.FileInfo) bool {
		// とりあえずぜんぶtrue
		return true
	}, 0)
	params := templatingParams{
		AppName:     appName,
		Controllers: botw.GetAllControllerNames(pkgs["controllers"]),
	}
	tpl, _ := template.New("tmp/main").Parse(MAIN)
	tpl.Execute(writer{}, params)

	// ここでmain.mainのソースコードが完成したので、tmp/mainに書き込む
	// 今あるものを消す
	tmpMainPath := filepath.Join(appPath, "tmp", "main.go")
	_ = os.Remove(filepath.Join(tmpMainPath))
	// 新しくつくる
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
	if e := cmd.Start(); e != nil {
		fmt.Println("App start failed: ", e)
		return
	}
	fmt.Println("App started")

	// なんかあるまではこっちのプロセスで監視してる
	finisher := make(chan bool)
	go func() {
		time.Sleep(10 * time.Second)
		finisher <- true
	}()

	select {
	case <-finisher:
		cmd.Process.Kill()
		fmt.Println("App Ended")
		return
	}
}

const MAIN = `// AUTO GENERATED MAIN PROCESS
// DO NOT EDIT
package main

import "github.com/otiai10/botw"
import "github.com/otiai10/twistream"
import "fmt"

import "{{.AppName}}/controllers"
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
    c := &botw.Controller{
        TL: timeline,
    }
    fmt.Println(c)

	{{range .Controllers}}
	botw.AppendController(&controllers.{{.}}{c})
	{{end}}
	e := <- botw.Serve()
    panic(e.Error())
}
`
