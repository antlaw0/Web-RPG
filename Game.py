def processCommand(command):
	cmd=command.split(" ")
	if cmd[0] == "test":
		return "test successful"
	elif cmd[0] == "test" and cmd[1] == "2":
		return "Second test successful"
	else:
		return "Command not recognized"