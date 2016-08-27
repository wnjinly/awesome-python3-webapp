#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
	summary = '为什么不显示出来,你大爷的'
	blogs = [
		Blog(id='1',name='Test Blog',summary=summary, created_at=time.time()-120),
		Blog(id='2',name='Something New',summary=summary, created_at=time.time()-3600),
		Blog(id='3',name='Learn Swift',summary=summary, created_at=time.time()-7200)
	]
	return {
		'__template__': 'blogs.html',
		'blogs': blogs
	}