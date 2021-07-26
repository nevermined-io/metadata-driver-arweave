[![banner](https://raw.githubusercontent.com/nevermined-io/assets/main/images/logo/banner_logo.png)](https://nevermined.io)

# metadata-driver-arweave

>    🐳  [Arweave](https://www.arweave.org/)) driver for MetadataDB (Python).
> [nevermined.io](https://nevermined.io)

[![PyPI](https://img.shields.io/pypi/v/nevermined-metadata-driver-arweave.svg)](https://pypi.org/project/nevermined-metadata-driver-arweave/)
[![Python package](https://github.com/nevermined-io/metadata-driver-arweave/workflows/Python%20package/badge.svg)](https://github.com/nevermined-io/metadata-driver-arweave/actions)

---

## Table of Contents

  - [Features](#features)
  - [Quickstart](#quickstart)
  - [Environment variables](#environment-variables)
---

## Features

Arweave driver for MetadataDB.

## Quickstart

In the configuration we are going to specify the following parameters to

```yaml
    [metadatadb]

    enabled=true                            # In order to enable or not the    plugin
    module=arweave                          # You can use one the plugins       already created. Currently we have elasticsearch, mongodb and bigchaindb, arweave.
    module.path=                            # You can specify the location of your custom plugin.
    db.hostname=https://arweave.net         # Address of your arweave instance.
    db.port=443                             # Port of your Elasticsearch rest API.
    db.wallet_file_path=./arweave-key.json # Path to the arweave wallet key
```

Once you have defined this the only thing that you have to do it is use it:

```python

    metadatadb = MetadataDB(conf)
    metadatadb.write({"value": "test"}, id)

```

## Environment variables

When you want to instantiate an Metadatadb plugin you can provide the next environment variables:

- **$CONFIG_PATH**
- **$MODULE**
- **$DB_HOSTNAME**
- **$DB_PORT**
- **$DB_INDEX**
- **$DB_WALLET_FILE_PATH**

## Testing

Automatic tests are setup via Github actions.
Our test use pytest framework.

## License

```
Copyright 2020 Keyko GmbH
This product includes software developed at
BigchainDB GmbH and Ocean Protocol (https://www.oceanprotocol.com/)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```