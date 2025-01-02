import multichain
import json

# Blockchain connection details
rpcuser = "multichainrpc"
rpcpassword = "2WYg41tyV5tDo6pcJqa3viFxGkNQYLuk81z8CrEbbtAW"
rpchost = "127.0.0.1"
rpcport = 4400
chainname = "khan"

# Initialize MultiChainClient
mc = multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

# Specify the stream name
stream_name = "user_registration"               

# Fetch stream items
stream_items = mc.liststreamitems(stream_name)

if not stream_items:
    print(f"No data found in the stream {stream_name}")
else:
    for item in stream_items:
    # Assuming the data is stored in 'data' and is JSON-encoded
        raw_data = item['data']['json']
        
        # Now, you can access and print it in a cleaner way
        try:
            formatted_data = json.dumps(raw_data, indent=4)  # Pretty print the JSON data
            print(formatted_data)
        except Exception as e:
            print(f"Error formatting data: {e}")

