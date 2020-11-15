os: mac
app: com.citrix.XenAppViewer
-

start [<user.text>]:
	key(ctrl-esc)
	sleep(500ms)
	insert(text or "")

workspace setup:
	key(ctrl-esc)
	sleep(500ms)
	insert("h:m")
	sleep(100ms)
	key(return)

hyperspace nonproduction:
	key(ctrl-esc)
	sleep(500ms)
	insert("H:\\Hyperspace nonproduction.RDP")
	sleep(100ms)
	key(return)

chart search [<user.text>]:
	key(ctrl-space)
	insert(text or "")