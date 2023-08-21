# Netskope-Python
Python tool to interface with Netskope API

# Examples for usage
How to use the API

See [main.py](https://github.com/ChubbsPeterson/Netskope-Python/blob/main/main.py) for examples

Example:

Import endpoint
```
from endpoints.endpoint_steering import Steering
```
Define tenant specific variables
```
TENANT = 'tenant_name'
BASE_URL = f"https://{TENANT}.goskope.com/api/v2" 
AUTH_TOKEN = "token_here"
```
Initialize endpoint class
```
# Initialize individual endpoints
steering_client = Steering(base_url=BASE_URL, auth_token=AUTH_TOKEN)
```
Query an endpoint
```
# display_output=True will print a formatted json response
steering_client.get_gre_pops(display_output=True) # Get all GRE POPs
```
OR
```
gre_pops = steering_client.get_gre_pops() # Get all GRE POPs
print(gre_pops)
```