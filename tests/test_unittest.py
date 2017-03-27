# -*- coding: utf-8 -*-

from pelican_comment_system import deep_set_default


def test_deep_set_default():
    key = "KEY"
    root_dict = {
        key: {
            '1': {
                '1.1': "X"
            },
            '2': "Y",
            '4': "Z"
        }
    }
    default_dict = {
        '1': {
            '1.1': "A",
            '1.2': {
                '1.2.1': "B"
            }
        },
        '2': "C",
        '3': "D"
    }
    expected_dict = {
        key: {
            '1': {
                '1.1': "X",
                '1.2': {
                    '1.2.1': "B"
                }
            },
            '2': "Y",
            '3': "D",
            '4': "Z"
        }
    }
    deep_set_default(root_dict, key, default_dict)
    assert root_dict == expected_dict
