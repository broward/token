# State Depository Token (SDT) Platform

Creating a digital token platform backed by a State-regulated depository similar to Texas bills [H.B. 1049](https://legiscan.com/TX/sponsors/HB1049/2025) and [H.B. 1056](https://legiscan.com/TX/bill/HB1056/2025) and [Wyoming's stablecoin](https://stabletoken.wyo.gov/).

[White paper](https://broward.ghost.io/current-gold-paper)

[History](https://broward.ghost.io/2024/11/26/sdt-history/)

[Research & Design](https://broward.ghost.io/token/)

![SDTOverview](https://github.com/broward/token/blob/main/docs/SDTOverview.jpg)

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



