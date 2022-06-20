import json

import requests

base_url = "http://0.0.0.0:5000"


def create_configs():
    """
    API client to create a new config for the given service
    Service-id in this example is: "abc"
    config-type/config-name is "emails"

    url = "{base_url}/adobe/v1/{service-id}/configs/emails"
    :return:
    """
    url = f"{base_url}/adobe/v1/abc/configs/emails"

    payload = json.dumps(
        {"config": {"enabled": True, "domains": "gmail.com, yahoo.com"}}
    )
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_all_configs():
    """
    API client to get all configs for a given service
    Service-id in this example is: "abc"

    url = "{base_url}/adobe/v1/{service-id}/configs"
    :return:
    """
    url = f"{base_url}/adobe/v1/abc/configs"

    headers = {"Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers)

    print(response.text)


def get_specific_configs():
    """
    API client to get specific config for the given service
    Service-id in this example is: "abc"
    config-type/config-name is "emails"

    url = "{base_url}/adobe/v1/{service-id}/configs/{config-name}"
    :return:
    """
    url = f"{base_url}/adobe/v1/abc/configs/emails"
    headers = {"Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers)

    print(response.text)


def update_service_config():
    """
    API client to update specific config for the given service
    Service-id in this example is: "abc"
    config-type/config-name is "emails"

    url = "{base_url}/adobe/v1/{service-id}/configs/{config-name}"
    :return:
    """
    url = f"{base_url}/adobe/v1/abc/configs/emails"

    payload = json.dumps(
        {"config": {"enabled": True, "domains": "gmail.com, yahoo.com, hotmail.com"}}
    )
    headers = {"Content-Type": "application/json"}
    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    create_configs()
    get_all_configs()
    get_specific_configs()
    update_service_config()
