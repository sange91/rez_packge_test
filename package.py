name = "mypackage"
version = "1.0"
build_command = False


def commands():
    global env
    env["MYVARIABLE"] = "YES"
    env["PYTHONPATH"].prepend("{root}")
    env["PYTHONPATH"].prepend("{root}/python")
