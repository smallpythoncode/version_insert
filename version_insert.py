""""
Inserts the version of projects as a comment to the top  line of
'requirements.txt' files located in the project docs directory. This script
should be ran from the project root (containing the README).
"""

# --- Development Links ---
# https://stackoverflow.com/questions/5137497/
# https://stackoverflow.com/questions/12332975/
# https://stackoverflow.com/questions/54462479/

import os
import subprocess
import sys
from _version import __version__

sphinx = ['alabaster', 'Babel', 'certifi', 'chardet', 'colorama', 'docutils',
          'idna', 'imagesize', 'Jinja2', 'm2r2', 'MarkupSafe', 'mistune',
          'packaging', 'Pygments', 'pyparsing', 'pytz', 'requests', 'six',
          'snowballstemmer', 'Sphinx', 'sphinxcontrib-applehelp',
          'sphinxcontrib-devhelp', 'sphinxcontrib-htmlhelp',
          'sphinxcontrib-jsmath', 'sphinxcontrib-qthelp',
          'sphinxcontrib-serializinghtml', 'urllib3']

reqs_docs_file = "subprotest_docs.txt"
reqs_file = "subprotest.txt"

# docs_present =


# subprocess.run([sys.executable, "-m", "pip", "freeze", ">", reqs_docs_file],
#                shell=True)

this_dir = os.getcwd()
# print(this_dir)
dir_split = this_dir.split("\\")
# print(dir_split)
# source code directory should be the same as project name
project_name = dir_split[-1]
print(project_name)

with open(reqs_docs_file, "r") as rdf:
    contents = rdf.readlines()

contents.insert(0, "# " + project_name + " - v" + __version__ + "\n")

print(contents)

with open(reqs_docs_file, "w") as rdf:
    contents = "".join(contents)
    rdf.write(contents)

list = ["a", "#", "b"]
list.sort()
print(list)







# # # is requirements for docs
#
# # path to _version.py
#

