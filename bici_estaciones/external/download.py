import requests

from click import progressbar
from clint.textui import progress


URL = 'http://cdn.buenosaires.gob.ar/datosabiertos/datasets/bicicletas-publicas/recorridos-realizados-2018.csv'
db = 'https://www.dropbox.com/pri/get/recorridos.csv?_download_id=2543180643112364265092847566998068430551915822378199030774352989&_notify_domain=www.dropbox.com&_subject_uid=65353973&w=AAB4f2D3HbAIcc4FeSBcm_c9OlD53dwFJdqdpS6JcLdZKw'


def downloader(path: str):
    headers = {
        'Host': 'cdn.buenosaires.gob.ar',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'DNT': '1',
        'Cookie': 'BIGipServerPool_varnish - cdn_prd = 3808564234.20480.0000',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es-419;q=0.7,es;q=0.6',
    }
    r = requests.get(URL, headers=headers, stream=True, timeout=300)
    with open(path, 'wb') as f:
        total_length = 475243
        for chunk in progress.bar(r.iter_content(chunk_size=512), expected_size=total_length):
            if chunk:
                f.write(chunk)
                f.flush()


# def d(path: str):
#     r = requests.get(URL, stream=True)
#     with open(path, 'wb') as f:
#         total_length = 243324273
#         for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
#             if chunk:
#                 f.write(chunk)
#                 f.flush()