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
# https://stackoverflow.com/questions/10507230/

# Boolean
# https://www.w3schools.com/python/python_booleans.asp
# https://stackoverflow.com/questions/5119709/


import os
import subprocess
import sys
# from _version import __version__

# The packages utilized for Sphinx documentation
# Parent installs: Sphinx==3.2.1, m2r2==0.2.5; the rest install from Sphinx
sphinx = ['alabaster', 'Babel', 'certifi', 'chardet', 'colorama', 'docutils',
          'idna', 'imagesize', 'Jinja2', 'm2r2', 'MarkupSafe', 'mistune',
          'packaging', 'Pygments', 'pyparsing', 'pytz', 'requests', 'six',
          'snowballstemmer', 'Sphinx', 'sphinxcontrib-applehelp',
          'sphinxcontrib-devhelp', 'sphinxcontrib-htmlhelp',
          'sphinxcontrib-jsmath', 'sphinxcontrib-qthelp',
          'sphinxcontrib-serializinghtml', 'urllib3']

root_dir = os.getcwd()
project_name = ""
req_docs_file = "docs/subprotest_docs.txt"
req_file = "docs/subprotest.txt"
good_paths = False


def get_project_name():
    dir_split = root_dir.split("\\")
    global project_name
    project_name = dir_split[-1]


def path_check():
    docs_present = os.path.isdir(root_dir + "\\docs")
    ver_present = os.path.isfile(root_dir + "\\_version.py")
    if not docs_present:
        print(root_dir + "\\docs not found.\n" +
              "Ensure this directory is present and rerun script.")
    elif not ver_present:
        print(root_dir + "\\" + project_name + "\\_version.py not found.\n" +
              "Ensure version file is present and rerun script.")
    else:
        global good_paths
        good_paths = True


# def req_docs_create():
#     try:
#         subprocess.run([sys.executable, "-m", "pip", "freeze", ">",
#                         reqs_docs_file], shell=True)
#     except FileNotFoundError:
#         print("Could not create requirements file.\n" +
#               "Ensure docs directory is present in root.")

# def reqs_docs_create():
#     subprocess.run([sys.executable, "-m", "pip", "freeze", ">",
#                     reqs_docs_file], shell=True)
#     print("reqs_docs created")



# with open(reqs_docs_file, "r") as rdf:
#     contents = rdf.readlines()

# contents.insert(0, "# " + project_name + " - v" + __version__ + "\n")

# print(contents)

# with open(reqs_docs_file, "w") as rdf:
#     contents = "".join(contents)
#     rdf.write(contents)

# list = ["a", "#", "b"]
# list.sort()
# print(list)


# # # is requirements for docs
#
# # path to _version.py
#

if __name__ == "__main__":
    print("Project root: " + root_dir + "\n")
    # subprocess.run([sys.executable, "-m", "pip", "freeze", ">",
    #                 req_docs_file], shell=True)
    get_project_name()
    path_check()
    if good_paths:
        print("Good to go.")
    print(os.path.isfile(".\\_version.py"))

# as it sits meow, this would require that the '_version.py' be located in the
# source directory. Should it be left this way? Or, should a condition be made
# to check if having the version file exist simply within a module and not a
# package necessarily?
