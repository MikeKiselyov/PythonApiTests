#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import base

login_url = str(base.url) + "/api/auth/login"

headers_with_referer = {
    'Referer': str(base.url) + "/bo/login"
}


def get_bearer_for_user(ADMIN, PASSWORD):
    data = "grant_type=password&username=" + ADMIN + "&password=" + PASSWORD
    response = requests.post(login_url, data=data, headers=headers_with_referer)
    all_information = response.json()
    get_token = all_information['access_token']
    bearer_token = {'Content-Type': "application/json",
                    'Authorization': "Bearer " + get_token}
    return bearer_token


admin_bearer = get_bearer_for_user("admin@admin.com", "qwerty123")
