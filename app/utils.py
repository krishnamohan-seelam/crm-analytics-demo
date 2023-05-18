import tomli
import sys
import json
import numpy as np
from pathlib import Path

TOML_CONFIG_PATH = "config/app_config.toml"
FAKE_DATA_PATH = "data/constituency.json"



def add_app_path():
    sys.path.append(str(Path(__file__).parents[1].absolute()))


def load_config(toml_file_path):
    with open(toml_file_path, mode="rb") as fp:
        config = tomli.load(fp)
        return config


def validate_config(config):
    if config is None:
        raise ValueError("TOML configuration is missing")


def load_data(file_path):
    with open(file_path, "r") as fp:
        return json.load(fp)
