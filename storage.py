import os
from azure.storage.blob import BlobServiceClient


def uploadBlob(container_name, blob_name, data):
    try:
        connect_str = os.getenv('STORAGE_STRING')
        container_name = str(container_name)
        blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
        blob_client = blob_service_client.get_blob_client(
            container=container_name, blob=blob_name)
        blob_client.upload_blob(data)
    except Exception as ex:
        print('Exception:')
        print(ex)


def genBlobContainer(name):
    connect_str = os.getenv('STORAGE_STRING')
    try:
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
        container_name = str(name)
        # Create the container
        blob_service_client.create_container(container_name)

    except Exception as ex:
        print('Exception:')
        print(ex)
