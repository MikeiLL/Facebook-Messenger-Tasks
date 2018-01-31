#!/usr/bin/python

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MIKE_EMAIL = os.environ.get("MIKE_EMAIL")
MIKE_PASS = os.environ.get("MIKE_PASS")
JOHN_EMAIL = os.environ.get("JOHN_EMAIL")
JOHN_PASS = os.environ.get("JOHN_PASS")
JIM_EMAIL = os.environ.get("JIM_EMAIL")
JIM_PASS = os.environ.get("JIM_PASS")
