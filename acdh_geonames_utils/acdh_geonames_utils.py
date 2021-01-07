"""Main module."""
import os
import zipfile
import requests
import pandas as pd

from . config import GN_DL_URL, GN_PL_HEADERS


def download_country_zip(country_code, out_dir='temp'):
    """
    downloads a geonames country zip like e.g.\
        http://download.geonames.org/export/dump/AT.zip \
            and returns the location of the zipped file

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


def unzip_country_zip(zipped_file):
    """
    unzipps a geonames country zip like e.g.\
        temp/AT.zip and returns the filename of the unzipped file

    :param country_code: The location of the zipped file e.g. temp/AT.zip
    :type country_code: str

    :return: The unzipped file e.g. temp/AT.txt
    :rtype: str
    """
    if zipped_file:
        path_name, file_name = os.path.split(zipped_file)
        with zipfile.ZipFile(zipped_file, "r") as zip_ref:
            zip_ref.extractall(path_name)
            unzipped_file = zipped_file.replace('.zip', '.txt')
    else:
        unzipped_file = ""
    return unzipped_file


def download_and_unzip_country_zip(country_code, out_dir='temp'):
    """
    downloads and unzipps a geonames country zip like e.g.\
        http://download.geonames.org/export/dump/AT.zip \
            and returns the filename of the unzipped file

    :param country_code: The country code of the country to download e.g. AT
    :type country_code: str

    :param out_dir: a directory path to store the downloaded file
    :type out_dir: str

    :return: The path of the downloaded and extracted zip
    :rtype: str
    """

    zipped_file = download_country_zip(country_code, out_dir=out_dir)
    if zipped_file:
        unzipped = unzip_country_zip(zipped_file)
    else:
        unzipped = ""
    return unzipped


def countries_as_df(input_file):
    """
    returns a geonames-download file as pandas Dataframe objects

    :param input_file: The location of an unzipped geonames\
        file e.g. temp/AT.txt
    :type input_file: str

    :return: a pandas.Dataframe objects
    :rtype: pandas.Dataframe
    """

    df = pd.read_csv(input_file, sep='\t', names=GN_PL_HEADERS)
    return df


def donwload_to_df(country_code, out_dir='temp'):
    """
    downloads and unzipps a geonames country zip like e.g.\
        http://download.geonames.org/export/dump/AT.zip \
            and returns the data as pandas.DataFrame

    :param country_code: The country code of the country to download e.g. AT
    :type country_code: str

    :param out_dir: a directory path to store the downloaded file
    :type out_dir: str

    :return: The data as pandas.DataFrame
    :rtype: `pandas.DataFrame`
    """

    input_file = download_and_unzip_country_zip(country_code, out_dir=out_dir)
    if input_file:
        df = countries_as_df(input_file)
    else:
        df = None
    return df
