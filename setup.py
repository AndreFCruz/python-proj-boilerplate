import re
from pathlib import Path
from setuptools import setup, find_packages


def stream_requirements(fd):
    """For a given requirements file descriptor, generate lines of
    distribution requirements, ignoring comments and chained requirement
    files.
    """
    for line in fd:
        cleaned = re.sub(r'#.*$', '', line).strip()
        if cleaned and not cleaned.startswith('-r'):
            yield cleaned


def load_requirements(txt_path):
    """Short helper for loading requirements from a .txt file.

    Parameters
    ----------
    txt_path : Path or str
        Path to the requirements file.

    Returns
    -------
    list
        List of requirements, one list element per line in the text file.
    """
    with Path(txt_path).open() as requirements_file:
        return list(stream_requirements(requirements_file))


# ---------------------------------------------------------------------------- #
#                                   Requirements                               #
# ---------------------------------------------------------------------------- #

ROOT_PATH = Path(__file__).parent
README_PATH = ROOT_PATH / 'README.md'

REQUIREMENTS_PATH = ROOT_PATH / 'requirements' / 'main.txt'
REQUIREMENTS_TEST_PATH = ROOT_PATH / 'requirements' / 'test.txt'

requirements = load_requirements(REQUIREMENTS_PATH)
requirements_test = load_requirements(REQUIREMENTS_TEST_PATH)


# ---------------------------------------------------------------------------- #
#                                   Version                                    #
# ---------------------------------------------------------------------------- #
SRC_PATH = ROOT_PATH / 'src' / 'my_project'
VERSION_PATH = SRC_PATH / '_version.py'

with VERSION_PATH.open('rb') as version_file:
    exec(version_file.read())


# ---------------------------------------------------------------------------- #
#                                   SETUP                                      #
# ---------------------------------------------------------------------------- #
setup(
    name="my-project-andre",
    version=__version__,
    description="Example boilerplate for a simple Python project",
    keywords=["boilerplate"],

    long_description=(README_PATH).read_text(),
    long_description_content_type="text/markdown",

    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['tests', 'tests.*']),
    package_data={
        '': ['*.yaml, *.yml'],
    },
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=requirements,
    tests_require=requirements_test,

    author="AndreFCruz",
    url="https://github.com/AndreFCruz/python-proj-boilerplate",

    license='GPL',

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
)