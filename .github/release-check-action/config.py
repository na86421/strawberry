import os


RELEASE_FILE_PATH = "RELEASE.md"
GITHUB_SHA = os.environ["GITHUB_SHA"]
GITHUB_EVENT_PATH = os.environ["GITHUB_EVENT_PATH"]
GITHUB_WORKSPACE = os.environ["GITHUB_WORKSPACE"]
API_URL = os.environ["API_URL"]