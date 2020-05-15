# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/356blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
#template = {
#    "name": "Galileo",
#    "type": "local",
#    "path": "../Galileo"
#}
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "duck356/356blog@gh-pages"
}

# 站点设置
site_name = "356的个人博客"
site_logo = "${static_prefix}logo.jpeg"
site_build_date = "2020-01-01T02:54+08:00"
author = "三百五十六"
email = "youngjie999@gmail.com"
author_homepage = "http://duck356.github.io/356blog/"
description = "16 * 55 = 28"
key_words = ['Duck356', '三百五十六', 'blog']
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

#valine = {
#    "enable": True,
#    "el": '#vcomments',
#    "appId": "h3aV05RdMCndeLiGf3dectNO-gzGzoHsz",
#    "appKey": "7UvgAfRhQitsCdoGCMy4lGxj",
#    "visitor": True,
#    "recordIP": True,
#    "highlight":True,
#    "recordIP":True,
#    "avatar": "robohash"
#}

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "h3aV05RdMCndeLiGf3dectNO-gzGzoHsz",
    "appKey": "7UvgAfRhQitsCdoGCMy4lGxj",
    "visitor": True,
    "recordIP": True,
    "highlight": True,
    "recordIP": True,
    "emojiCDN": '//i0.hdslb.com/bfs/emote/',
    "emojiMaps": {
        "tv_doge": "6ea59c827c414b4a2955fe79e0f6fd3dcd515e24.png",
        "tv_亲亲": "a8111ad55953ef5e3be3327ef94eb4a39d535d06.png",
        "tv_偷笑": "bb690d4107620f1c15cff29509db529a73aee261.png",
        "tv_再见": "180129b8ea851044ce71caf55cc8ce44bd4a4fc8.png",
        "tv_冷漠": "b9cbc755c2b3ee43be07ca13de84e5b699a3f101.png",
        "tv_发怒": "34ba3cd204d5b05fec70ce08fa9fa0dd612409ff.png",
        "tv_发财": "34db290afd2963723c6eb3c4560667db7253a21a.png",
        "tv_可爱": "9e55fd9b500ac4b96613539f1ce2f9499e314ed9.png",
        "tv_吐血": "09dd16a7aa59b77baa1155d47484409624470c77.png",
        "tv_呆": "fe1179ebaa191569b0d31cecafe7a2cd1c951c9d.png",
        "tv_呕吐": "9f996894a39e282ccf5e66856af49483f81870f3.png",
        "tv_困": "241ee304e44c0af029adceb294399391e4737ef2.png",
        "tv_坏笑": "1f0b87f731a671079842116e0991c91c2c88645a.png",
        "tv_大佬": "093c1e2c490161aca397afc45573c877cdead616.png",
        "tv_大哭": "23269aeb35f99daee28dda129676f6e9ea87934f.png",
        "tv_委屈": "d04dba7b5465779e9755d2ab6f0a897b9b33bb77.png",
        "tv_害羞": "a37683fb5642fa3ddfc7f4e5525fd13e42a2bdb1.png",
        "tv_尴尬": "7cfa62dafc59798a3d3fb262d421eeeff166cfa4.png",
        "tv_微笑": "70dc5c7b56f93eb61bddba11e28fb1d18fddcd4c.png",
        "tv_思考": "90cf159733e558137ed20aa04d09964436f618a1.png",
        "tv_惊吓": "0d15c7e2ee58e935adc6a7193ee042388adc22af.png",
        # 更多表情
    }
}


head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = 'Posted by:三百五十六'

body_addon = ''

background_img = "../src/Mononoke_Hime.jpg"
