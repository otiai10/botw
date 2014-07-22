package main

import (
	"fmt"
	"github.com/otiai10/flagg"
	"go/build"
	"os"
	"os/exec"
	"path/filepath"
)

// 開発用
import (
	"time"
)

type Command interface {
	Execute()
}

type CommandRun struct{}

func (cRun CommandRun) Execute() {
	// {{{ TODO: DRY
	gopath := build.Default.GOPATH
	appName := flagg.Arg(1)
	// }}}
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
