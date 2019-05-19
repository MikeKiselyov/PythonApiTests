#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose
import requests
import json
import unittest
import authentication
import base

if __name__ == "__main__":
    nose.main()

create_order = open("json/sectional_title_residential_plus_insurance_Valuation.json").read()
admin_bearer = authentication.admin_bearer


def create_new_order():
    response = requests.post(base.url + "/api/Orders/Order", data=create_order, headers=base.header_content_type)
    token_for_order = response.json()
    return token_for_order


new_order = create_new_order()


class BaseTestCase(unittest.TestCase):
    def test_positive_check_order(self):
        response = requests.get(base.url + "/api/Orders/Edit?orderId=" + new_order, headers=admin_bearer)
        base.assert_correct_response(response, base.SUCCESS, 'GET')
        get_response = json.dumps(response.json())
        get_parsed_json = json.loads(get_response)
        get_parsed_json['isPaymentProofed'] = True
        dumps_to_json = json.dumps(get_parsed_json)
        response_checked_checkbox = requests.post(base.url + "/api/Orders/Edit",
                                                  data=dumps_to_json, headers=admin_bearer)
        base.assert_correct_response(response_checked_checkbox, base.SUCCESS, 'GET')
        id_for_order = "{\"orderId\":\"" + new_order + "\",\"serviceNumber\":0}"
        response_submit_order = requests.post(base.url + "/api/orders/SubmitReport", data=id_for_order,
                                              headers=admin_bearer)
        base.assert_correct_response(response_submit_order, base.SUCCESS, 'GET')
