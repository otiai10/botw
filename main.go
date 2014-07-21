package main

import "github.com/otiai10/botw/cmd"
import "github.com/otiai10/flagg"

// import "github.com/otiai10/twistream"

func main() {
	flagg.Parse()
	cmd := getCmd(flagg.Arg(0))
	cmd.Execute()
}

var commandRegistry = map[string]botw.Command{
	"new":  botw.CommandNew{},
	"run":  botw.CommandRun{},
	"love": botw.CommandRun{},
	"help": botw.CommandHelp{},
}

func getCmd(subcommand string) botw.Command {
	if cmd, ok := commandRegistry[subcommand]; ok {
		return cmd
	}
	return commandRegistry["help"]
}
