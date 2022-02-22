name = "mypackage"
version = "2.0"
build_command = "python {root}/install.py"


def commands():
    global env
    env["MYVARIABLE"] = "YES"
    env["PYTHONPATH"].prepend("{root}")
    env["PYTHONPATH"].prepend("{root}/source")
