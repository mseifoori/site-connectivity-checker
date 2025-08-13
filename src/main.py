import threading
import requests

def site_connectivity_checker(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>'
        }
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            print(f'{url} is available!')
            return True
        else:
            print(f'{url} is not available at this time!')
    except requests.exceptions.RequestException as e:
        print(f'Failed to reach {url}! Error: {e}')

websites_to_check = []

threads = []
for url in websites_to_check:
    thread = threading.Thread(target=site_connectivity_checker, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    