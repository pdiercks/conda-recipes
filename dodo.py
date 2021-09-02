import pathlib
from doit.tools import run_once

ROOT = pathlib.Path(__file__).parent
PACKAGES = {
    "pypi": {
        "pygmsh": "6.1.1",
        "neovim-remote": "2.4.0",
        "betterbib": "4.0.0",
    }
}


def task_pypi_packages():
    """generate recipes for packages available from pypi"""
    for package, version in PACKAGES["pypi"].items():
        yield {
            "name": package,
            "actions": [f"grayskull pypi {package}=={version}"],
            "targets": [ROOT / package / "meta.yaml"],
            "uptodate": [run_once],
            "clean": True,
        }
