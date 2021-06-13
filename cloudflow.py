from azure.storage.blob import BlobClient
from datetime import datetime, timedelta


connection_string = "DefaultEndpointsProtocol=https;AccountName=bawsla;AccountKey=PypW7LePRrAFTWZR/8OuiS9i/wNZvLkgR53XfqGJpgPUqWxl5szJu+xS1s2nG9AW64PEm7TT30Fr/XnNkKtmXw==;EndpointSuffix=core.windows.net"
	
# init azure blob storage connection
def init_blob_conn(container_name, blob_name):
	blob = BlobClient.from_connection_string(conn_str=connection_string, container_name=container_name, blob_name=blob_name)
	return blob

# upload blob
def upload_blob(container_name, blob_name, filepath):
	blob = init_blob_conn(container_name, blob_name)
	with open(filepath, 'rb') as data:
		blob.upload_blob(data)
	return True
	
