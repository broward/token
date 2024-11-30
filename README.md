# State Depository Token (SDT) Platform

Creating a digital token platform backed by a State-regulated depository similar to Texas bills S.B. No. 2334 and H.B. No. 4903. 

[White paper](https://broward.ghost.io/current-gold-paper)

[History](https://broward.ghost.io/2024/11/26/sdt-history/)

[Research & Design](https://broward.ghost.io/token/)

![SDTOverview](https://github.com/user-attachments/assets/1864dcd5-c548-4b09-9125-a3ec9dedf996)

1) OpenAPI creates message schemas and REST definitions.
2) Python generates the working code.
3) Client sends a transaction message plus a private key shard.
4) REST API accepts the message and queues it to SQS.
5) API retrieves 2nd key shard from RDS.
6) API submits it all to Nitro Enclave.
7) The embedded Fireblocks library retrieves 3rd key shard.
8) Fireblocks executes MPC on assembled key to validate.
9) Nitro Enclave returns result to API.
10) API writes entry to Quorum blockchain.
11) API returns result to client.



