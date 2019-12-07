#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import orm
import random
from models import User, Blog, Comment

async def test(loop):

	await orm.create_pool(loop=loop, user='developer', password='develop', db='awesome')

	u = User(name='test', email='test@example.com', password='888888', image='about:blank')

	await u.save()

async def test_get(loop):

	await orm.create_pool(loop, user='developer', password='develop', db='awesome')

	U = await User().findAll()

	print(U)

async def create_user(loop):
	await orm.create_pool(loop = loop, user = 'developer', password = 'develop', db = 'awesome')

	admin = User(name='Admin', email='admin@example.com', password='admin', image='about:blank')
	await admin.save()

	willam = User(name='Willam', email='hsiehwangkuei@163.com', password='willam', image='about:blank')
	await willam.save()

if __name__ == "__main__":

	loop = asyncio.get_event_loop()

	tasks = [create_user(loop)]

	loop.run_until_complete(asyncio.wait(tasks))

	loop.close()

	print('Test finished')