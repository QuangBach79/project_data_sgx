import os
import logging
import time
import requests
import datetime

if not os.path.exists('/Users/thieuquangbach/Desktop/project_data_sgx/log1'):
    os.makedirs('/Users/thieuquangbach/Desktop/project_data_sgx/log1')

logging.basicConfig(level=logging.INFO, handlers=[
    logging.FileHandler("/Users/thieuquangbach/Desktop/project_data_sgx/log1/download.log"),
    logging.StreamHandler()
])

def download_file(url, save_path, file_name):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(save_path,'wb') as file:
                file.write(response.content)
            logging.info(f'Successfully downloaded' + file_name)
            return True
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'An error occurred: {err}')
        time.sleep((2 ** (attempt + 1)) * 60)
    logging.error(f'Failed to download {url} after 3 attempts.')
    return False

def downloads(url_list, date_file):
    recovery_list = set()
    for url in url_list:
        # file_id = url.split('/')[-2]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        if url.split('/')[-1] == "WEBPXTICK_DT.zip" or url.split('/')[-1] == "TC_.txt" :
            file_name = f'{current_date}_'+url.split('/')[-1]+'_'+date_file
        else:
            file_name = f'{current_date}_'+url.split('/')[-1]
        save_path = f"/Users/thieuquangbach/Desktop/project_data_sgx/{file_name}"

        if not download_file(url, save_path, file_name):
            recovery_list.add(url+f'/{date_file}')
    return recovery_list
