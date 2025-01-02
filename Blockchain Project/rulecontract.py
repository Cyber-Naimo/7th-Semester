# -*- coding: utf-8 -*-
"""
Updated on Sun Nov 28 19:24:29 2024
"""

import json
import base64
import multichain

# Blockchain connection details
rpcuser = "multichainrpc"
rpcpassword = "2WYg41tyV5tDo6pcJqa3viFxGkNQYLuk81z8CrEbbtAW"
rpchost = "127.0.0.1"
rpcport = 4400
chainname = "khan"

# Initialize the MultiChainClient
mc = multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

# Define streams
weather_stream = "weather_alerts"
user_stream = "user_registration"

# Create the streams
try:
    mc.create('stream', weather_stream, True)  # Weather alerts stream
    mc.create('stream', user_stream, True)  # User registration stream
    print(f"Streams '{weather_stream}' and '{user_stream}' created.")
except Exception as e:
    print(f"Error creating streams: {e}")

# Subscribe to the streams
try:
    mc.subscribe(weather_stream)
    mc.subscribe(user_stream)
    print(f"Subscribed to streams '{weather_stream}' and '{user_stream}'.")
except Exception as e:
    print(f"Error subscribing to streams: {e}")

# Function to register a user
def register_user(username, password, role):
    try:
        user_data = {
            "username": username,
            "password": password,  # Hash the password in production
            "role": role
        }
        txid = mc.publish(user_stream, username, {"json": user_data})
        print(f"User '{username}' registered with txid: {txid}")
    except Exception as e:
        print(f"Error registering user: {e}")

# Example: Registering users
register_user("weather_alert", "secure_password", "admin")
register_user("disaster_manager", "password123", "viewer")
