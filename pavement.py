from paver.easy import *
from paver.setuputils import setup
from multiprocess import Process
import platform
import json

setup(
    name = "pytest-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("PyTest Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/pytest-browserstack",
    packages=['tests']
)

def run_py_test(config, task_id=0):
    if platform.system() == "Windows":
        sh('cmd /C "set CONFIG_FILE=resources/%s.json && set TASK_ID=%s && set REMOTE=true && pytest -s src/test/suites/*.py --driver Browserstack -n 1"' % (config, task_id))
    else:
        sh('CONFIG_FILE=resources/%s.json TASK_ID=%s REMOTE=true pytest -s src/test/suites/*.py --driver Browserstack -n 2' % (config, task_id))

@task
@consume_nargs(1)
def run(args):
    """Run single, local and parallel test using different config."""
    jobs = []
    config_file = 'resources/%s.json' % (args[0])
    with open(config_file) as data_file:
        CONFIG = json.load(data_file)
    environments = CONFIG['environments']
    for i in range(len(environments)):
        p = Process(target=run_py_test, args=(args[0], i))
        jobs.append(p)
        p.start()
