import pytest
from browserstack.local import Local
import os, json
from jsonmerge import merge
from dotenv import load_dotenv
import time

load_dotenv()

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'resources/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0


with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

bs_local = None
timenow = None

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG["user"]
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG["key"]

def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    global timenow
    timenow=str(time.time()*1000)
    print(timenow)
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY or "access_key", "localIdentifier": timenow }
    bs_local.start(**bs_local_args)

def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()

if os.environ['REMOTE'] == "true":
  @pytest.fixture(scope='session')
  def session_capabilities():
    global timenow
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0].split('::')[1]
    capabilities = merge(CONFIG['environments'][TASK_ID],CONFIG["capabilities"])
    capabilities['bstack:options']['userName'] = BROWSERSTACK_USERNAME
    capabilities['bstack:options']['accessKey'] = BROWSERSTACK_ACCESS_KEY
    capabilities['bstack:options']['source'] = 'pytest:sample-main:v1.0'
    capabilities['bstack:options']['sessionName'] = test_name
    print(CONFIG['base_url'])
    if "local" in capabilities['bstack:options'] and capabilities['bstack:options']['local']:
      start_local()
      capabilities['bstack:options']['localIdentifier'] = timenow
    return capabilities

@pytest.fixture(scope='session')
def base_url():
  print(CONFIG['base_url'])
  return CONFIG['base_url']

def pytest_sessionfinish(session, exitstatus):
  stop_local()

