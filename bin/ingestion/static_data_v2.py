import requests
import time
def download_url(url, save_path):
    '''
 Purpose: Download a zip file of fantasy football data.
 First try using the requests library to access the site.
 If that fails, sleep for 5 seconds then re-try.
 Finally, iterate through the file and write it to the intended directory
     '''
    try:
        r = requests.get(url, stream=True)
    except:
        time.sleep(5)
    finally:
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=100):
                fd.write(chunk)
download_url(
    'https://www.fantasyfootballdatapros.com/static/data_v2.zip',
             'static_data_v2.zip'
)