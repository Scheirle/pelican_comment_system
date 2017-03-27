# -*- coding: utf-8 -*-

import os
import logging
from pelican import Pelican
from pelican.settings import read_settings


#logger = logging.getLogger(__name__)
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
FULLSITE_SOURCE_PATH = os.path.join(CURRENT_PATH, 'fullsite_source')
FULLSITE_EXPECTED_PATH = os.path.join(CURRENT_PATH, 'fullsite_expected')
FULLSITE_CONFIG = os.path.join(FULLSITE_SOURCE_PATH, "pelicanconf.py")


def recursive_file_list(root_dir, sub_dir=""):
    full_dir_path = os.path.join(root_dir, sub_dir)
    assert os.path.isdir(full_dir_path)
    files = []
    for file in os.listdir(full_dir_path):
        full_file_path = os.path.join(full_dir_path, file)
        local_file_path = os.path.join(sub_dir, file)
        if os.path.isdir(full_file_path):
            files.extend(recursive_file_list(root_dir, local_file_path))
        else:
            files.append(str(local_file_path))
    return files


def assert_dir_equal(expected_dir, tmpdir):
    expected_dir = os.path.abspath(expected_dir)
    tmpdir = os.path.abspath(tmpdir)

    expected_files = sorted(recursive_file_list(expected_dir))
    tmp_files = sorted(recursive_file_list(tmpdir))

    assert expected_files == tmp_files
    for file in expected_files:
        expected_file_path = os.path.join(expected_dir, file)
        tmp_file_path = os.path.join(tmpdir, file)

        with open(expected_file_path, 'r', encoding='utf-8') as ef:
            with open(tmp_file_path, 'r', encoding='utf-8') as tf:
                assert ef.read() == tf.read()


def test_fullsite(tmpdir, caplog):
    caplog.set_level(logging.DEBUG)
    overrides = {
        'OUTPUT_PATH': str(tmpdir)
    }
    pelican = Pelican(
        settings=read_settings(path=FULLSITE_CONFIG, override=overrides)
    )
    pelican.run()
    assert_dir_equal(FULLSITE_EXPECTED_PATH, str(tmpdir))
