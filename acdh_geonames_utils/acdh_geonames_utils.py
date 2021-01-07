"""Main module."""
import os
import requests

from . config import GN_DL_URL


def download_country_zip(country_code, out_dir='temp'):
    """
    downloads a geonames country zip like e.g.\
        http://download.geonames.org/export/dump/AT.zip

    :param country_code: The country code of the country to download e.g. AT
    :type country_code: str

    :param out_dir: a directory path to store the downloaded file
    :type out_dir: str

    :return: The path of the downloaded zip
    :rtype: str
    """
    url = f"{GN_DL_URL}{country_code}.zip"
    file_name = f"{country_code}.zip"
    save_path = f"{os.path.join(out_dir, file_name)}"
    os.makedirs(out_dir, exist_ok=True)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
        return save_path
    else:
        return ""
