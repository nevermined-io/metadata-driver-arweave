import arweave
from requests import api
from metadatadb_driver_interface.utils import get_value
from metadatadb_driver_interface.exceptions import ConfigError, MetadataDbError

_DB_INSTANCE = None


def get_database_instance(config_file=None):
    global _DB_INSTANCE
    if _DB_INSTANCE is None:
        _DB_INSTANCE = ArweaveInstance(config_file)

    return _DB_INSTANCE


class ArweaveInstance:
    def __init__(self, config=None):
        host = get_value(
            "db.hostname", "ARWEAVE_HOSTNAME", "https://arweave.net", config
        )
        port = get_value("db.port", "ARWEAVE_PORT", None, config)
        wallet_file_path = get_value(
            "db.wallet_file_path", "ARWEAVE_WALLET_FILE_PATH", None, config
        )

        if wallet_file_path is None:
            raise ConfigError("Wallet file not found.")

        api_url = f"{host}:{port}" if port is not None else host

        try:
            self.wallet = arweave.Wallet(wallet_file_path)
        except Exception as e:
            raise MetadataDbError(f"Error instantiating arweave wallet: {str(e)}")

        self.wallet.api_url = api_url
