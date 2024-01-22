


def smart(source:str):
    from smart_open import open
    from google.cloud.storage import Client
    import os
    service_account_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    client = Client.from_service_account_json(service_account_path)
    fin = open(f'{source}', transport_params=dict(client=client))
    return fin