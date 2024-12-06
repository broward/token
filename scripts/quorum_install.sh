sudo apt update
# sudo apt install nodejs ??
sudo apt install npm
npx quorum-dev-quickstart

sudo systemctl start docker --memory=5g
run 'run.sh' in the directory, './quorum-test-network'


List endpoints and services
----------------------------------
JSON-RPC HTTP service endpoint                 : http://localhost:8545
JSON-RPC WebSocket service endpoint            : ws://localhost:8546
Web block explorer address                     : http://localhost:25000/explorer/nodes
Prometheus address                             : http://localhost:9090/graph
Grafana address                                : http://localhost:3000/d/a1lVy7ycin9Yv/goquorum-overview?orgId=1&refresh=10s&from=now-30m&to=now&var-system=All
Collated logs using Grafana and Loki           : http://localhost:3000/d/Ak6eXLsPxFemKYKEXfcH/quorum-logs-loki?orgId=1&var-app=quorum&var-search=



