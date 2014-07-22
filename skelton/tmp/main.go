// ここのコードはrun時にapppathを解析した結果自動生成されるものなので
// 将来的にはunkoとか書かない
// Developerもここは全くいじらない
package main

import "github.com/otiai10/botw"

// ここは{appname}
import "unko/controllers"
import "unko/conf"

func main() {
	botw.InitVars(
		conf.CONSUMERKEY,
		conf.CONSUMERSECRET,
		conf.ACCESSTOKEN,
		conf.ACCESSTOKENSECRET,
	)
	// ここ抽象的にController取れるの？
	botw.AppendController(&controllers.Sample{})
	botw.Serve()
}
