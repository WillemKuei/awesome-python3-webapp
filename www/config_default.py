#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Override configurations.
'''

__author__ = 'Willam'

configs = {
	'debug': True,
	'db': {
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'developer',
		'password': 'develop',
		'db': 'awesome'
	},
	'session': {
		'secret': 'Awesome'
	}
}