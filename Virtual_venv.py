import subprocess
import sys


def create_env(env_name):
    subprocess.run([sys.executable, '-m', 'venv', env_name])


def install_packages(path, packages_name:list):
    subprocess.run([path, 'install', *packages_name])


