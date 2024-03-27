from suds.client import Client

# Define the WSDL URL of the SOAP service
wsdl_url = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls?WSDL'

# Create a SOAP client
client = Client(wsdl_url)

# Call the functions provided by the SOAP service
result1 = client.service.Method1()
result2 = client.service.Method2()
# Call other methods as needed...

# Process the responses
print("Result of Method1:", result1)
print("Result of Method2:", result2)
# Process other responses as needed...
