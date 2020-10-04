""""
A script to generate source and Sphinx requirements files with version comments

1. Generates 'docs/requirements_docs.txt' to document sphinx requirements
2. Inserts the version of the project as a comment to the top  line of
'requirements_docs.txt' located in the project docs directory.


Notes:
- Script should be ran from the project root (containing the README).
- Requires that the 'docs/' and '<source>/_version.py' be present
  - Exceptions implemented
"""

# --- Development Links ---
# https://stackoverflow.com/questions/5137497/
# https://stackoverflow.com/questions/12332975/
# https://stackoverflow.com/questions/54462479/

# Boolean
# https://www.w3schools.com/python/python_booleans.asp
# https://stackoverflow.com/questions/5119709/


import os
import subprocess
import sys
from _version import __version__

# The packages utilized for Sphinx documentation
# Parent installs: Sphinx, m2r2; the rest install from Sphinx
sphinx = ['alabaster', 'Babel', 'certifi', 'chardet', 'colorama', 'docutils',
          'idna', 'imagesize', 'Jinja2', 'm2r2', 'MarkupSafe', 'mistune',
          'packaging', 'Pygments', 'pyparsing', 'pytz', 'requests', 'six',
          'snowballstemmer', 'Sphinx', 'sphinxcontrib-applehelp',
          'sphinxcontrib-devhelp', 'sphinxcontrib-htmlhelp',
          'sphinxcontrib-jsmath', 'sphinxcontrib-qthelp',
          'sphinxcontrib-serializinghtml', 'urllib3']

this_dir = os.getcwd()
reqs_docs_file = "docs/subprotest_docs.txt"
reqs_file = "docs/subprotest.txt"
docs_present = False


def get_project_name():
    dir_split = this_dir.split("\\")
    # print(dir_split)
    # source code directory should be the same as project name
    project_name = dir_split[-1]
    print(project_name)


def docs_detect():
    docs_present = os.path.isdir(this_dir + "\\docs")


# def version_present():


subprocess.run([sys.executable, "-m", "pip", "freeze", ">", reqs_docs_file],
               shell=True)

with open(reqs_docs_file, "r") as rdf:
    contents = rdf.readlines()

# contents.insert(0, "# " + project_name + " - v" + __version__ + "\n")

print(contents)

with open(reqs_docs_file, "w") as rdf:
    contents = "".join(contents)
    rdf.write(contents)

# list = ["a", "#", "b"]
# list.sort()
# print(list)



# # # is requirements for docs
#
# # path to _version.py
#

if __name__ == "__main__":
    get_project_name()
    docs_detect()
    if docs_present:
        print("Docs present")
    else:
        print("You fucked up")
