import json
import requests
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

# OpenWeather API details
API_KEY = "fcc21c8ab9e4d5c1da659ec891cf7bc7"
LATITUDE = 24.8607
LONGITUDE = 67.0011
url = f"http://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}"

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
def check_authorization(role, required_role="admin"):
    if role == required_role:
        print("Authorization successful.")
        return True
    print("Authorization failed.")
    return False

# Fetch weather data
def fetch_weather_data():
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

# Check for bad weather conditions
def check_bad_weather(data):
    conditions = data['weather'][0]['main']
    if conditions in ['Thunderstorm', 'Rain', 'Snow', 'Drizzle', 'Smoke']:
        return True, conditions
    return False, conditions

# Authenticate and authorize user
username = "weather_alert"
password = "secure_password"

authenticated, role = authenticate_user(username, password)
if authenticated and check_authorization(role):
    weather_data = fetch_weather_data()
    if weather_data:
        is_bad_weather, condition = check_bad_weather(weather_data)
        if is_bad_weather:
            alert_message = f"Alert: Severe weather detected: {condition}"
            print(alert_message)
            try:
                mc.publish(weather_stream, "weather_alert", {"json": {"description": alert_message}})
                print("Weather alert published.")
            except Exception as e:
                print(f"Error publishing weather alert: {e}")
        else:
            print(f"Weather condition is {condition}. No alert needed.")
else:
    print("Access denied.")
