package main

import "github.com/otiai10/gobotter/gobotter"
import "github.com/otiai10/flagg"

// import "github.com/otiai10/twistream"

func main() {
	flagg.Parse()
	cmd := getCmd(flagg.Arg(0))
	cmd.Execute()
}

var commandRegistry = map[string]gobotter.Command{
	"new":  gobotter.CommandNew{},
	"run":  gobotter.CommandRun{},
	"love": gobotter.CommandRun{},
	"help": gobotter.CommandHelp{},
}

func getCmd(subcommand string) gobotter.Command {
	if cmd, ok := commandRegistry[subcommand]; ok {
		return cmd
	}
	return commandRegistry["help"]
}
