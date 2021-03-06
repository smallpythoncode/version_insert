""""
A script to generate separate source-only and source plus Sphinx requirements
files with version comments.

1.  Retrieves the project name.
2.  Verifies that the docs directory exists and creates one if it does not


x. Generates 'docs/requirements_docs.txt' to document sphinx
requirements
x. Inserts the version of the project as a comment to the top  line of
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
# variable import
# https://stackoverflow.com/questions/6677424/
# Boolean
# https://www.w3schools.com/python/python_booleans.asp
# https://stackoverflow.com/questions/5119709/


import os
# from importlib import import_module
# import subprocess
# import sys
# from ver import __version__
# from version_insert._version import __version__




# The packages utilized for Sphinx documentation
# Parent installs: Sphinx==3.2.1, m2r2==0.2.5; the rest install from Sphinx
sphinx = ['alabaster', 'Babel', 'certifi', 'chardet', 'colorama', 'docutils',
          'idna', 'imagesize', 'Jinja2', 'm2r2', 'MarkupSafe', 'mistune',
          'packaging', 'Pygments', 'pyparsing', 'pytz', 'requests', 'six',
          'snowballstemmer', 'Sphinx', 'sphinxcontrib-applehelp',
          'sphinxcontrib-devhelp', 'sphinxcontrib-htmlhelp',
          'sphinxcontrib-jsmath', 'sphinxcontrib-qthelp',
          'sphinxcontrib-serializinghtml', 'urllib3']

root = os.getcwd()
docs = root + "\\docs"
project_name = ""
ver_path = root + "_version.py"
good_paths = False
version = ""

# req_docs_file = "docs/subprotest_docs.txt"
# req_file = "docs/subprotest.txt"


def get_project_name(cwd=os.getcwd()):
    """Returns project name from last level of current working directory.

    :param cwd: current working directory
    :type cwd: str
    :return: project name
    :rtype: str
    """
    import os
    name = cwd.split("\\")
    return name[-1]


def docs_ensure(docs_dir):
    """Checks that the project's docs directory exists and creates it if it
    doesn't.

    :param docs_dir: project's docs directory
    :type docs_dir: str
    """
    docs_present = os.path.isdir(docs_dir)
    if not docs_present:
        os.mkdir(docs_dir)


def ver_check():
    """Checks access to project version module

    :return:
    """
    global project_name
    project_name = get_project_name(root)
    assert os.path.isdir(docs), \
        "Ensure " + root + "\\docs is present."
    # global is_package
    is_package = os.path.isdir(root + "\\" + project_name)
    # TODO - exception for no __init__ in package
    # TODO - exception for ._version.py not present
    try:
        global version
        if is_package:
            version = getattr(__import__(project_name + "._version",
                              fromlist="__version__"), "__version__")
        else:
            version = getattr(__import__("_version", fromlist="__version__"),
                              "__version__")
    except ModuleNotFoundError:
        print("")
    # else:
    #     ver_present = "bumpy"
    # print()

    # elif not ver_present:
    #     if is_package:
    #         print(package_ver_path + " not found.\n"
    #               "Ensure version file is present and rerun script.")
    #     else:
    #         print(module_ver_path + " not found.\n"
    #               "Ensure version file is present and rerun script.")
    # else:
    #     global good_paths
    #     good_paths = True


def path_check_test():

    print("Project name: " + project_name)


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

# if __name__ == "__main__":
#     print("Project root: " + root_dir + "\n")
#     # subprocess.run([sys.executable, "-m", "pip", "freeze", ">",
#     #                 req_docs_file], shell=True)
#     get_project_name()
#     path_check()
#     if good_paths:
#         print("Good to go.")
#         print(__version__)


if __name__ == "__main__":
    path_check()
    assert (len(project_name) > 0), \
        "Project name not defined, run path_check()"
    # print("Project name: " + project_name)
    # path_check()
    # print("Project name: " + project_name)
    # print(ver)



# 1st week october
# as it sits meow, this would require that the '_version.py' be located in the
# source directory. Should it be left this way? Or, should a condition be made
# to check if having the version file exist simply within a module and not a
# package necessarily?
