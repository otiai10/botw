package main

import "github.com/otiai10/flagg"

// import "github.com/otiai10/twistream"

func main() {
	flagg.Parse()
	cmd := getCmd(flagg.Arg(0))
	cmd.Execute()
}

var commandRegistry = map[string]Command{
	"new":  CommandNew{},
	"run":  CommandRun{},
	"love": CommandRun{},
	"help": CommandHelp{},
}

func getCmd(subcommand string) Command {
	if cmd, ok := commandRegistry[subcommand]; ok {
		return cmd
	}
	return commandRegistry["help"]
}
