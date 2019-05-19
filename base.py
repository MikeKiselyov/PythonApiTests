#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testconfig import config

SUCCESS = 200
CLIENT_ERROR = 400
SERVER_ERROR = 500

url = config['url']

header_content_type = {'Content-type': 'application/json'}


def assert_correct_response(response, response_code, method):
    if response.status_code == response_code:
        assert True
    else:
        print('Request:\n' + str(response.url) + '\nfailed')
        print('Method => ' + str(method))
        print('ACTUAL RESULT: ' + str(response.status_code))
        print('EXPECTED RESULT: ' + str(response_code))
        print(response.json())
        assert False
