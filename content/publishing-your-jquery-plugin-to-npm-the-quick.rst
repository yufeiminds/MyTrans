发布插件到NPM的快捷和复杂方法
=============================

:description: 当我们要把一个插件注册到jQuery官方库的时候, 
:date: 2012-12-12 12:12
:tags: jQuery

目前如果你不使用npm，jQuery官方插件库就只能读取现有的插件。并且我们推荐转到 ``npm`` 来发布插件。

如果你正在阅读这篇文章，我猜你正在选择一种插件发布器，我们希望使这个过程变得尽可能地轻松。

你也许听说过 ``npm`` 使用可浏览和Web包的方式使前端开发变得更轻松。我们在这篇文章中将不重述它的任何优点。取而代之的是，我们只关注那些帮助你注册软件包到 ``npm`` 仓库，以便于他人下载的那些知识，并且我们会及时更新这篇文章。

开始前
------

你需要做如下的事情：

1. 安装Node.js
2. 执行 ``npm install -g npm`` 来更新 ``npm``

使用命令行登录
--------------

为了发布到 ``npm`` 仓库，你需要一个 ``npm`` 账户，并且通过命令行登录它。

首先，确认你是否已经通过运行:

    npm whoami

登录它。

如果你已经登陆，它会显示你的用户名。或者显示 ``Not authed`` ，那就执行 ``npm adduser`` 。

这行 ``npm adduser`` 命令可以用来创建一个用户，或者通过一个已经存在的账户登录，它会分别提示你输入用户名，密码，和电子邮件。

.. code-block:: bash

    $ npm adduser
      Username:
      Password:
      Email: (this IS public)

鉴权证书会存放在一个叫做 ``.npmrc`` 的文件中，所以你只需要登陆一次。

创建你的 package manifest
-------------------------

当你发布到 jQuery 插件库的时候，你需要在一个类似于 ``*.jquery.json`` 的文件中提供包信息。与此相同，你将需要提供一个 ``package.json`` 文件让 ``npm`` 识别你的包。

你可以重命名已经存在的 ``*.jquery.json`` 文件为 ``package.json`` ，并且更新其中的值，或者创建一个新的 ``package.json`` 。

重命名 ``*.jquery.json`` 到 ``package.json``
--------------------------------------------

在 ``*.jquery.json`` 和 ``package.json`` 之间有如下几点不同：

* 确认你添加了 ``jquery-plugin`` 和 ``ecosystem:jquery`` 作为关键字，它会帮助用户找到你的npm包。
* npm不使用 ``docs`` 这个键，取而代之，你可能希望使用 ``repository`` 指向你的repo 。
* npm 不使用 ``demo`` 键。
* npm 不使用 ``download`` 键。
* bugs 键可以指定一个字符串，而在 ``*.jquery.json`` 中，可以是存有 ``url`` 以及/或者 ``email`` 的对象。

.. attention:: 这句话需要确认

创建一个package.json *
----------------------

你可以切换到项目根目录，运行 ``npm init`` 自动生成一个 ``package.json`` 文件。 它会提示你回答一系列问题。

.. note:: 当提示输入关键字时，请确认添加了 ``jquery-plugin`` 和 ``ecosystem:jquery`` 。

发布你的包
----------

现在你已经准备好 ``package.json`` 了，可以把它发布到 npm 仓库中，npm使用像jQuery仓库那样的语义版本处理它，如果你对语义版本是如何工作的感兴趣，可以观看 `这段视频 <https://docs.npmjs.com/getting-started/semantic-versioning>`_ ，我们也有一段视频关于 `如何发布 <https://docs.npmjs.com/getting-started/publishing-npm-packages>`_ 的知识。

如果是基于语义版本规则，你需要为你的包创建一个新的版本，或者在 ``package.json`` 中更改版本号，或者运行 ``npm version <type>`` ，举个例子，对于创建一个发布版本的补丁，你会使用 ``npm version patch`` ，它会在你的 ``package.json`` 里增加版本号，并且在你的 *git repo* 上打上一个标签。

做完这些之后，运行 ``npm publish`` 发布你的包到npm仓库中，如果一切正常，你应该会在 ``npmjs.com/package/package_name`` 上看到一个关于你的包的页面。

如果你还需要任何帮助，可以通过 `我们的推特 <https://twitter.com/npm_support>`_ 或者 `电子邮件 <support@npmjs.com>`_ 获取支持。

下一小节
--------

在下一篇文章里，我们将涉及如何用 npm 下载jQuery插件并且将其应用在你的项目中。

译文
^^^^

**原文** : http://blog.npmjs.org/post/111475741445/publishing-your-jquery-plugin-to-npm-the-quick

**Japanese** : https://medium.com/@watilde/%E7%BF%BB%E8%A8%B3-publishing-your-jquery-plugin-to-npm-the-quick-and-dirty-way-8487344e2b3f
