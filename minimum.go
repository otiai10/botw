package botw

import (
	"fmt"
	"time"
)

func Serve() {
	// アプリケーションのmain thread
	for {
		fmt.Println(time.Now())
		time.Sleep(1 * time.Second)
	}
}
