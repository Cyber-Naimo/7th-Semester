import multichain

# Blockchain connection details
rpcuser = "multichainrpc"
rpcpassword = "2WYg41tyV5tDo6pcJqa3viFxGkNQYLuk81z8CrEbbtAW"
rpchost = "127.0.0.1"
rpcport = 4400
chainname = "khan"

# Initialize MultiChainClient
mc = multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

# Define streams
policy_stream = "access_policies"

# Publish access policy
def publish_access_policy():
    try:
        policy = {
            "target": {
                "subject.role": {"@in": ["admin", "viewer"]},
                "resource.type": {"@eq": "weather_alert"},
                "action": {"@in": ["create", "view"]}
            },
            "effect": "PERMIT"
        }
        txid = mc.publish(policy_stream, "weather_alert_policy", {"json": policy})
        print(f"Access policy published with txid: {txid}")
    except Exception as e:
        print(f"Error publishing access policy: {e}")

# Publish the policy
publish_access_policy()
