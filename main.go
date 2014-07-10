package main

import "github.com/otiai10/hisyotan/hisyotan"
import "github.com/otiai10/flagg"
// import "github.com/otiai10/twistream"

func main() {
    flagg.Parse()
    cmd := getCmd(flagg.Arg(0))
    cmd.Execute()
}

var commandRegistry = map[string]hisyotan.Command {
    "run": hisyotan.CommandRun{},
    "help": hisyotan.CommandHelp{},
}

func getCmd(subcommand string) hisyotan.Command {
    if cmd, ok := commandRegistry[subcommand]; ok {
        return cmd
    }
    return commandRegistry["help"]
}
