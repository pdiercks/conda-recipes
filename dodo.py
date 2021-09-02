import pathlib

ROOT = pathlib.Path(__file__).parent
PACKAGES = {
    "pypi": {
        "pygmsh": "6.1.1",
        "neovim-remote": "2.4.0",
    }
}


def task_pypi_packages():
    """generate recipes for packages available from pypi"""
    for package, version in PACKAGES["pypi"].items():
        yield {
            "name": package,
            "actions": [f"grayskull pypi {package}=={version}"],
            "targets": [ROOT / package / "meta.yml"],
            "clean": True,
        }
