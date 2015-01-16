from fabric.api import local, lcd, task, sudo, hosts, settings, execute, run
import getpass
import os.path

project_name = "myproject"

HERE = os.path.dirname(__file__)
BUILDS_PATH = os.path.abspath(os.path.join(HERE, "builds"))
SRC_PATH = os.path.abspath(os.path.join(HERE, "src"))
DEV_TMP_NAME = "current_dev"
DEV_TMP_PATH = os.path.join(BUILDS_PATH, DEV_TMP_NAME)

@task
def create(version, type="prod"):
    name = type + "_" + version
#    if type != "dev":
#        with lcd(SRC_PATH):
#            git_check_no_modifs() 
#            if not is_current_git_branch_named("master"):
#                print "You are not on the master branch.. you can't deploy"
#                raise
#            local("git tag "+name)
#            local("git push --tags")
    build(name)

@task
def update():
    with lcd(SRC_PATH):
        git_check_no_modifs()
        if is_current_git_branch_named("master"):
            print "Warning: you may not want to be on master branch"
        local("git pull")
    build(DEV_TMP_NAME)
    link(DEV_TMP_NAME, "dev")

@task 
def build(name):
    if name == DEV_TMP_NAME:
        # prevent error on first call
        local("mkdir -p "+DEV_TMP_PATH)
        local("rm -rf "+DEV_TMP_PATH)
    with lcd(SRC_PATH):
        local("meteor build ../builds/"+name+"/ --directory")
    SRC_DIR = os.path.join(BUILDS_PATH, name)
    serv = os.path.join(SRC_DIR, "bundle/programs/server")
    with lcd(serv):
        local("npm install")

@task
def link(version, type="prod"):
    name = type + "_" + version
    if version == DEV_TMP_NAME:
        name = DEV_TMP_NAME
    DEPLOY_DIR = "./" + type
    SRC_DIR = os.path.abspath(os.path.join(HERE, "builds/"+name))
    local("rm "+DEPLOY_DIR)
    local("ln -s "+SRC_DIR+" "+DEPLOY_DIR+"") 
    local("sudo service "+project_name+" restart")
    
@task
def deploy(version, type="prod"):
    create(version, type)
    link(version, type)
    print "deployed "+version

def git_check_no_modifs():
    try:
        local("git diff --no-ext-diff --quiet --exit-code")
    except:
        print "Repository has modifications: exiting." 
        raise

def is_current_git_branch_named(name):
    branch = local("git branch | grep ^\*", True)
    isMaster = branch == "* "+name
    return isMaster
