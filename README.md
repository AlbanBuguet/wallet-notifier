# wallet-notifier

A Lambda function that listens to the flight events of `flight-status-events`, and pushes the gate changes and the delays to the passes in the wallets, through `wallet-pass-signer`.

## Test it

```sh
pip install -r requirements.txt && pytest
```
