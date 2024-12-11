# State Depository Token (SDT) Platform

A digital token platform backed by State-regulated depositories similar to Texas bills [H.B. 1049](https://legiscan.com/TX/sponsors/HB1049/2025) and [H.B. 1056](https://legiscan.com/TX/bill/HB1056/2025) and [Wyoming's stablecoin](https://stabletoken.wyo.gov/).

My goal is to create this system via State funding‚ grants‚ consulting, etc. [My background is eclectic](https://broward.ghost.io/2014/03/09/about/) and spans startups‚ corporations‚ State and Federal systems for 35 years.

[White paper](https://broward.ghost.io/current-gold-paper)

[History](https://broward.ghost.io/2024/11/26/sdt-history/)

[Research & Design](https://broward.ghost.io/token/)

![SDTOverview](https://github.com/broward/token/blob/main/docs/APIOverview.jpg)

Components defined and justified for State Depository Token Platform:

ACH, KYC & AML: [3rd-party API development](https://broward.ghost.io/2024/11/28/sdt-kyc-and-aml/)\
Language: [Python ver 3.9](https://broward.ghost.io/2024/11/26/sdt-language/) - [Ubuntu install](https://askubuntu.com/questions/1318846/how-do-i-install-python-3-9)\
Blockchain: [Quorum](https://broward.ghost.io/2024/11/26/sdt-blockchain-3/) - [QuickStart](https://docs.goquorum.consensys.io/tutorials/quorum-dev-quickstart/using-the-quickstart/), [Features](https://www.geeksforgeeks.org/quorum-blockchain/)\
Database: AWS RDS\
ORM: Prototype with [Peewee](https://broward.ghost.io/2024/11/28/sdt-orm/) - [https://github.com/coleifer/peewee](https://github.com/coleifer/peewee)\
Transport: [AWS Lambda](https://broward.ghost.io/2020/08/14/revision-2/)\
Security: [Indeterminate MPC Library](https://broward.ghost.io/2024/11/26/sdt-security/)
Queue: [AWS SQS](https://broward.ghost.io/2020/08/14/revision-2/)\
Vault: AWS Nitro Enclave\
Schema: [OpenAPI](https://broward.ghost.io/2024/11/27/sdt-schema/) - [Editor](https://swagger.io/tools/swagger-editor/download/)\
Stablecoin: [Custom work to extend Quorum](https://broward.ghost.io/2024/11/28/sdt-stablecoin/)\
Config Management: [Test out DynaConfig](https://www.dynaconf.com/)\
Integration Testing: [Test out Localsource](https://docs.localstack.cloud/user-guide/aws/feature-coverage/)\
Depositories: Some proprietary API work\
Other Tools: [Misc](https://broward.ghost.io/2024/11/28/sdt-misc-tools/)


**API PROCESS FLOW**

* ChatGBT create schemas, SQL DDL, REST apis and python API code.
* Client requests a transaction_id.
* Client sends a signed EDDSA transaction.
* REST API accepts the message and queues it to SQS
* API submits transaction to Blockchain Composite.
* Blockchain Composite returns result to API.
* API returns result to client.
* API updates depositories.

![BlockOverview](https://github.com/broward/token/blob/main/docs/BlockOverview.jpg)


**BLOCK COMPOSITE PROCESS FLOW**

* MPC Library generates/distributes key shards to three locations.
* API submits transaction to Blockchain Composite.
* MPC Library retrieves shards and assembles key.
* MPC Library validates transaction.
* MPC Library writes a chain entry to Quorum.
* Block Composite returns result to API.
