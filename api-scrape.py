import requests
from requests.exceptions import HTTPError

for url in ['https://www.bezrealitky.cz/api/record/markers?offerType=prodej&estateType=byt&locationInput=Praha']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

type(response)
response.json().items()
