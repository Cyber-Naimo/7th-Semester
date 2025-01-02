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
weather_stream = "weather_alerts"
user_stream = "user_registration"

# Authenticate user
def authenticate_user(username, password):
    try:
        stream_items = mc.liststreamitems(user_stream)
        for item in stream_items:
            user_data = item['data']['json']
            if user_data['username'] == username and user_data['password'] == password:
                print(f"User '{username}' authenticated successfully.")
                return True, user_data['role']
        print(f"Authentication failed for user '{username}'.")
        return False, None
    except Exception as e:
        print(f"Error authenticating user: {e}")
        return False, None

# Check authorization
def check_authorization(role, required_role="viewer"):
    if role == required_role or role == "admin":
        print("Authorization successful.")
        return True
    print("Authorization failed.")
    return False

# Fetch weather alerts
def fetch_weather_alerts():
    try:
        stream_items = mc.liststreamitems(weather_stream)
        if stream_items:
            return stream_items[-1]['data']['json']
    except Exception as e:
        print(f"Error fetching weather alerts: {e}")
    return None

# Authenticate and authorize user
username = "jane_doe"
password = "password123"

authenticated, role = authenticate_user(username, password)
if authenticated and check_authorization(role):
    alert = fetch_weather_alerts()
    if alert:
        print(f"Weather Alert: {alert['description']}")
    else:
        print("No alerts found.")
else:
    print("Access denied.")
