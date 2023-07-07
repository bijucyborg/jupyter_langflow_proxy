"""
Return config on servers to start for h2o-llm-studio

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_h2ollmstudio():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "logo.svg"
        )

    # Make sure executable is in $PATH
    def _get_h2ollmstudio_command(port):
        executable = "wave"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find h2ollmstudio executable in $PATH")
        # Create working directory
        home_dir = os.environ.get("HOME") or "/home/jovyan"
        working_dir = f"{home_dir}/h2o-llmstudio"
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:
            logger.info("Directory %s already exists" % working_dir)
        return ["wave", "run", "{working_dir}/app"]

    return {
        "command": _get_h2ollmstudio_command,
        "timeout": 20,
        "launcher_entry": {"title": "h2ollmstudio", "icon_path": _get_icon_path()},
    }