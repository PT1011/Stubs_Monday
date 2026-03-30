import os
import random
from datetime import datetime


# ============================================================
# INSTRUCTIONS
# ============================================================
# Each function below has a dependency problem.
# It reaches out to something external that your test cannot control.
#
# For each function:
#   1. Fix the function so the dependency can be injected
#   2. Write a test that passes every time
#
# Your fix must:
#   - add a parameter with default None
#   - use the real dependency only if the parameter is None
#
# Submit this file to Blackboard via GitHub link when done.
# ============================================================


# ------------------------------------------------------------
# Exercise 1 -- datetime dependency
# ------------------------------------------------------------
# This function checks whether a store is open based on the
# current time. A test that calls it without controlling the
# time will pass sometimes and fail sometimes.
#
# Fix: add a parameter so the time can be injected.
# Then write test_store_open() and test_store_closed() below.

def get_store_status():
    hour = datetime.now().hour
    if 9 <= hour < 21:
        return "Store is open"
    else:
        return "Store is closed"


def test_store_open():
    pass  # replace with your test


def test_store_closed():
    pass  # replace with your test


# ------------------------------------------------------------
# Exercise 2 -- random dependency
# ------------------------------------------------------------
# This function assigns a student to a study group at random.
# A test that calls it without controlling randomness cannot
# assert a specific result reliably.
#
# Fix: add a parameter so the random source can be injected.
# Then write test_assign_study_group() below.
# Use == to assert an exact value -- not "result in [...]"

def assign_study_group():
    return random.choice(["Group A", "Group B", "Group C"])


def test_assign_study_group():
    pass  # replace with your test


# ------------------------------------------------------------
# Exercise 3 -- environment variable dependency
# ------------------------------------------------------------
# This function returns an API URL based on an environment
# variable. A test that calls it without controlling the
# environment cannot predict which URL it gets back.
#
# Fix: add a parameter so the env value can be injected.
# Then write test_api_url_production() and
# test_api_url_staging() below.

def get_api_url():
    env = os.getenv("APP_ENV")
    if env == "production":
        return "https://api.example.com"
    else:
        return "https://staging.example.com"


def test_api_url_production():
    pass  # replace with your test


def test_api_url_staging():
    pass  # replace with your test
