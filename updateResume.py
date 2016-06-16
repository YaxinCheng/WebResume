#!/usr/local/bin/python3
from shutil import copyfile
import subprocess
copyfile("""/Users/Cheng/Documents/Dal/Fall 2015/Co-op/Résumé.pdf""", """/Users/Cheng/Developer/Python/Resume/static/resume.pdf""")
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Update Resume pdf file"])
subprocess.call(["git", "push", "heroku", "master"])

