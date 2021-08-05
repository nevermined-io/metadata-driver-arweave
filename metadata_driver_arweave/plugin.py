from json.decoder import JSONDecodeError
import logging
import json

from metadatadb_driver_interface.plugin import AbstractPlugin
from metadatadb_driver_interface.exceptions import MetadataDbError
import arweave

from metadata_driver_arweave.arweave_client import get_database_instance


class Plugin(AbstractPlugin):
    def __init__(self, config=None):
        self.driver = get_database_instance(config)
        self.logger = logging.getLogger("Plugin")
        logging.basicConfig(level=logging.INFO)

    @property
    def type(self):
        return "Arweave"

    def write(self, obj, resource_id=None):
        self.logger.debug("arweave::write::%s" % resource_id)
        data = json.dumps(obj).encode()

        try:
            transaction = arweave.Transaction(self.driver.wallet, data=data)
            transaction.add_tag("Content-Type", "application/json")
            transaction.sign()
            transaction.send()
        except Exception as e:
            raise MetadataDbError(f"Error posting {resource_id} to arweave: {str(e)}")

        return transaction.id

    def read(self, resource_id):
        self.logger.debug("arweave::read::%s" % resource_id)

        try:
            transaction = arweave.Transaction(self.driver.wallet, id=resource_id)
            transaction.get_transaction()
            transaction.get_data()
        except Exception as e:
            raise MetadataDbError(
                f"Error retrieving {resource_id} from arweave: {str(e)}"
            )

        try:
            return json.loads(transaction.data)
        except JSONDecodeError as e:
            raise MetadataDbError(f"Error decoding arweave data: {str(e)}")

    def update(self, obj, resource_id):
        self.logger.debug("arweave::update::%s" % resource_id)
        raise MetadataDbError("update operation is not available with arweave")

    def delete(self, resource_id):
        self.logger.debug("arweave::delete::%s" % resource_id)
        raise MetadataDbError("delete operation is not available with arweave")

    def list(self, search_from=None, search_to=None, limit=None):
        self.logger.debug("arweave::list")
        raise MetadataDbError("list operation is not available with arweave")

    def query(self, query_model):
        self.logger.debug("arweave::query")
        raise MetadataDbError("query operation is not available with arweave")

    def text_query(self, full_text_model):
        self.logger.debug("arweave::text_query")
        raise MetadataDbError("text_query operation is not available with arweave")

    def status(self, resource_id):
        self.logger.debug("arweave::status::%s" % resource_id)

        try:
            transaction = arweave.Transaction(self.driver.wallet, id=resource_id)
            status = transaction.get_status()

            if status != "PENDING":
                return "ACCEPTED"

            return status
        except Exception as e:
            raise MetadataDbError(
                f"Error retrieving the status of {resource_id} from arweave: {str(e)}"
            )
