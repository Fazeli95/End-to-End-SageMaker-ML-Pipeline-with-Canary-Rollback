
import boto3

def invoke_endpoint(endpoint_name, payload):
    runtime = boto3.client('sagemaker-runtime')
    response = runtime.invoke_endpoint(EndpointName=endpoint_name, ContentType='text/csv', Body=payload)
    return response['Body'].read()

if __name__ == "__main__":
    payload = 'your-csv-data-here'
    result = invoke_endpoint('your-endpoint-name', payload)
    print(result)
