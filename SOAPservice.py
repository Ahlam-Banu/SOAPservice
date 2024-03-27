from zeep import Client

# Define the WSDL URL of the SOAP service
wsdl_url = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls?WSDL'

# Create a SOAP client
client = Client(wsdl_url)

# Call the functions provided by the SOAP service
result1 = client.service.AddInteger(5, 10)  # Assuming AddInteger takes two integers as parameters
result2 = client.service.DivideInteger(10, 2)  # Assuming DivideInteger takes two integers as parameters
result3 = client.service.FindPerson("John Doe")  # Assuming FindPerson takes a string parameter

# Process the responses
print("Result of AddInteger:", result1)
print("Result of DivideInteger:", result2)
print("Result of FindPerson:", result3)
# Process other responses as needed...
