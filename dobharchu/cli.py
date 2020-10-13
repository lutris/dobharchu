"""Click configuration module"""
import os
import time
import click
import requests

SITE_URL = "http://localhost:8000"
TOKEN_PATH = os.path.expanduser("~/.cache/lutris/dobharchu.token")


@click.group()
def main():
    """Click entry point"""


@main.command()
@click.argument("username")
@click.argument("password")
def login(username, password):
    """Login to the Lutris API"""
    response = requests.post(SITE_URL + "/api/accounts/token", {
        "username": username,
        "password": password
    })
    response_data = response.json()
    if 'non_field_errors' in response_data:
        for error in response_data['non_field_errors']:
            print(error)
        return
    if 'token' in response_data:
        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(response_data["token"])
        print("Logged in as %s" % username)


def read_token():
    """Return the stored API token"""
    if not os.path.exists(TOKEN_PATH):
        return
    with open(TOKEN_PATH) as token_file:
        token = token_file.read().strip()
    return token


@main.command()
@click.argument("file_path")
@click.option("--url-prefix", required=True)
@click.option("--runtime", required=True)
def add_runtime_folder(file_path, url_prefix, runtime):
    """Scans a folder recursively and add every file as runtime component"""
    token = read_token()
    if not token:
        print("You need to login first")
    api_endpoint = SITE_URL + "/api/runtimes/" + runtime
    headers = {"Authorization": "Token %s" % token}
    if not file_path.endswith("/"):
        file_path += "/"

    for base, _dirs, files in os.walk(file_path):
        for _file in files:
            filename = os.path.join(base, _file)[len(file_path):]
            url = url_prefix + filename
            print("%s %s %s" % (runtime, filename, url))
            payload = {
                "url": url,
                "filename": filename
            }
            response = requests.post(api_endpoint, payload, headers=headers)
            print(response.status_code)
            time.sleep(0.3)  # Find out if an admin token can bypass rate limiting?
