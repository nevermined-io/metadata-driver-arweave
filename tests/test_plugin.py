import json

import arweave


def test_plugin_type(arweave_plugin):
    assert arweave_plugin.type == "Arweave"


def test_write(arweave_plugin, ddo_example):
    arweave_tx_id = arweave_plugin.write(ddo_example)

    transaction = arweave.Transaction(arweave_plugin.driver.wallet, id=arweave_tx_id)
    transaction.get_data()

    retrieved_ddo = json.loads(transaction.data)
    assert retrieved_ddo == ddo_example


def test_read(arweave_plugin, ddo_example):
    arweave_tx_id = arweave_plugin.write(ddo_example)

    retrieved_ddo = arweave_plugin.read(arweave_tx_id)
    assert retrieved_ddo == ddo_example


def test_status(arweave_plugin, ddo_example):
    arweave_tx_id = arweave_plugin.write(ddo_example)

    status = arweave_plugin.status(arweave_tx_id)
    assert status == "PENDING"
