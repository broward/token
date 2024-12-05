# State Depository Token (SDT) Platform

A digital token platform backed by State-regulated depositories similar to Texas bills [H.B. 1049](https://legiscan.com/TX/sponsors/HB1049/2025) and [H.B. 1056](https://legiscan.com/TX/bill/HB1056/2025) and [Wyoming's stablecoin](https://stabletoken.wyo.gov/).

My goal is to create this system via State funding‚ grants‚ consulting, etc. [My background is eclectic](https://broward.ghost.io/2014/03/09/about/) and spans startups‚ corporations‚ State and Federal systems for 35 years.

[White paper](https://broward.ghost.io/current-gold-paper)

[History](https://broward.ghost.io/2024/11/26/sdt-history/)

[Research & Design](https://broward.ghost.io/token/)

![SDTOverview](https://github.com/broward/token/blob/main/docs/SDTOverview.jpg)

Components defined and justified for State Depository Token Platform:

ACH, KYC & AML: [3rd-party API development](https://broward.ghost.io/2024/11/28/sdt-kyc-and-aml/)\
Language: [Python ver 3.9](https://broward.ghost.io/2024/11/26/sdt-language/) - [Ubuntu install](https://askubuntu.com/questions/1318846/how-do-i-install-python-3-9)\
Blockchain: [Quorum](https://broward.ghost.io/2024/11/26/sdt-blockchain-3/) - [QuickStart](https://docs.goquorum.consensys.io/tutorials/quorum-dev-quickstart/using-the-quickstart/), [Features](https://www.geeksforgeeks.org/quorum-blockchain/)
Database: AWS RDS
ORM: Prototype with [Peewee](https://broward.ghost.io/2024/11/28/sdt-orm/) - [https://github.com/coleifer/peewee](https://github.com/coleifer/peewee)
Transport: [AWS Lambda](https://broward.ghost.io/2020/08/14/revision-2/)
Security: [Fireblocks MPC](https://broward.ghost.io/2024/11/26/sdt-security/) - [Github](https://github.com/fireblocks/mpc-lib)
Queue: [AWS SQS](https://broward.ghost.io/2020/08/14/revision-2/)
Vault: AWS Nitro Enclave
Schema: [OpenAPI](https://broward.ghost.io/2024/11/27/sdt-schema/) - [Editor](https://swagger.io/tools/swagger-editor/download/)
Stablecoin: [Custom work to extend Quorum](https://broward.ghost.io/2024/11/28/sdt-stablecoin/)
Depositories: Probably proprietary API work
Other Tools: [Misc](https://broward.ghost.io/2024/11/28/sdt-misc-tools/)


**PROCESS FLOW**

1) OpenAPI and ChatGBT create message schemas, REST server and database DDL.
2) Python and ChatGBT generate the execution code.
3) Client sends a transaction message plus a private key shard.
4) REST API accepts the message and queues it to SQS.
5) API retrieves 2nd key shard from RDS.
6) API submits it all to Nitro Enclave.
7) The embedded Fireblocks library retrieves 3rd key shard.
8) Fireblocks executes MPC on assembled key to validate.
9) Nitro Enclave returns result to API.
10) API writes entry to Quorum blockchain.
11) API returns result to client.



