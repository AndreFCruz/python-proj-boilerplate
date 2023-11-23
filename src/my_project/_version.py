"""File to keep the package version in one place"""
from importlib import metadata

__version__ = metadata.version("my-project-andre")
__version_info__ = tuple(__version__.split("."))
