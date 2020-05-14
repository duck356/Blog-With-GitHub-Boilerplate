# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/356blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "duck356/356blog@gh-pages"
}

# 站点设置
site_name = "356的个人博客"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "三百五十六"
email = "youngjie999@gmail.com"
author_homepage = "http://duck356.github.io/356blog/"
description = "16 * 55 = 28"
key_words = ['Maverick', '三百五十六', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "三百五十六",
        "url": "http://duck356.github.io/356blog/",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "不懂就问",
        "url": "https://google.com",
        "brief": "不懂就问"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/duckduck356",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/duck356",
        "icon": "gi gi-github"
    },
#    {
#       "name": "Weibo",
#       "url": "https://weibo.com/5245109677/",
#       "icon": "gi gi-weibo"
#   }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "h3aV05RdMCndeLiGf3dectNO-gzGzoHsz",
    "appKey": "7UvgAfRhQitsCdoGCMy4lGxj",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
