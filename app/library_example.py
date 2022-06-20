from adobe_config_mgmt_lib.core.service_config import service_config_mgmt
from pydantic import BaseModel
from structlog import get_logger

logger = get_logger()


def get_all_configs():
    """Get all the configs for a given service"""
    res = service_config_mgmt.get_all_service_config(service_id="abc")
    logger.info(f"GET-ALL-CONFIGS: Received response: {res}")
    return res


def get_configs():
    """Get the specified configs for a given service"""
    res = service_config_mgmt.get_service_config_by_name(
        service_id="abc", config_name="emails"
    )
    logger.info(f"GET-SPECIFIC-CONFIGS: Received response: {res}")
    return res


def add_configs():
    """Add a new config for the given service"""
    config_data = {"config": {"enabled": True, "domains": "gmail.com, yahoo.com"}}

    class ServiceConfigPayload(BaseModel):
        config: dict = {}

    res = service_config_mgmt.add_service_config(
        service_id="abc",
        config_name="notification",
        config_data=ServiceConfigPayload(config=config_data),
    )
    logger.info(f"CREATE-NEW-CONFIGS: Received response: {res}")


def update_existing_configs():
    """Update an existing config for the given service"""
    config_data = {"config": {"enabled": True, "domains": "gmail.com, yahoo.com"}}
    res = service_config_mgmt.update_service_config(
        service_id="abc", config_name="notification", config=config_data
    )
    logger.info(f"UPDATE-CONFIGS: Received response: {res}")


if __name__ == "__main__":
    add_configs()
    get_all_configs()
    get_configs()
    update_existing_configs()
