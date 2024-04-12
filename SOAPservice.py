from zeep import Client

# Define the WSDL URL of the SOAP service
wsdl_url = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls?WSDL'

# Create a SOAP client
client = Client(wsdl_url)

#this is done from github.dev online
# Call the functions provided by the SOAP service
result1 = client.service.AddInteger(5, 10)
result2 = client.service.DivideInteger(10, 2)

# Process the responses
print("Result of AddInteger:", result1)
print("Result of DivideInteger:", result2)