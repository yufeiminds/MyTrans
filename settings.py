# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    "name": "Yufei's translation",  # your site name
    "url": "http://trans.thxminds.com",  # your site url
    # "prefix": "blog",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    "source": "content",
    "output": "deploy",
    "static": "deploy/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{filename}}.html",
    "relative_url": False,
    "perpage": 30,
    "feedcount": 20,
    "timezone": "+08:00",
}


author = {
    "default": "Yufei Li",
    "vars": {
        "Yufei Li": {
            "website": "http://blog.thxminds.com",
            "email": "yufeiminds@gmail.com",
            "github": "https://github.com/yufeiminds",
        }
    }
}

#: active readers
reader = {
    "active": [
        # "liquidluck.readers.markdown.MarkdownReader",
        # uncomment to activate rST reader
        "liquidluck.readers.restructuredtext.RestructuredTextReader",
    ],
    "vars": {}
}

#: active writers
writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        "liquidluck.writers.core.TagCloudWriter",
    ],
    "vars": {
        # uncomment if you want to reset archive page
        # "archive_output": "archive.html",
    }
}

#: theme variables
theme = {
    "name": "mathy",

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    "vars": {
        "disqus": "thxminds",
        "baidu_analytics": "d1d48c3d6a4ffd2b5a1fa405fbb1535a",
        # "analytics": "UA-21475122-1",
    }
}

#: template variables
template = {
    "vars": {},
    "filters": {},
}