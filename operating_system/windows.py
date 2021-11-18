from talon import Context, actions


ctx = Context()
ctx.matches = r"""
os: windows
"""

ctx.lists["self.launch_command"] = {
    "sound": "control mmsys.cpl sounds",
    "bluetooth": "control bthprops.cpl",
    "applications": "control appwiz.cpl",
    "display": "control desk.cpl",
    "taskbar": "control /name Microsoft.Taskbar",
    "programs and features": "control /name Microsoft.ProgramsAndFeatures",
    "Power": "control powercfg.cpl",
    "Mouse": "control main.cpl",
    "Network": "control /name Microsoft.NetworkAndSharingCenter",
    # "Notifications": "control /name Microsoft.NotificationAreaIcons",
}


@ctx.action_class("user")
class UserActionsWin:
    def exec(command: str):
        actions.user.system_command_nb(command)

    def system_shutdown():
        shutdown("s")

    def system_restart():
        shutdown("r")

    def system_hibernate():
        shutdown("h")

    def system_lock():
        actions.key("super-l")

    def system_show_desktop():
        actions.key("super-d")

    def system_task_view():
        actions.key("super-tab")

    def system_switcher():
        actions.key("ctrl-alt-tab")


def shutdown(flag: str):
    actions.key("super-r")
    actions.sleep("650ms")
    actions.insert(f"shutdown /{flag}")