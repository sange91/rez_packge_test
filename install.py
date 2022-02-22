# This script is called on `rez build`
import os
import shutil

print("Running install.py...")
root = os.path.dirname(__file__)
build_dir = os.environ["REZ_BUILD_PATH"]
install_dir = os.environ["REZ_BUILD_INSTALL_PATH"]

print("Copying payload to %s.." % build_dir)
shutil.copytree(
    os.path.join(root, "source"),
    os.path.join(build_dir, "source"),
    ignore=shutil.ignore_patterns("*.pyc", "__pycache__")
)

if int(os.getenv("REZ_BUILD_INSTALL")):
    # This part is called with `rez build --install`
    print("Installing payload to %s..." % install_dir)
    shutil.copytree(
        os.path.join(build_dir, "source"),
        os.path.join(install_dir, "source"),
    )