---
layout: post
title: formataddr() and unicode
date: 2011-02-11 14:44:07
tags:
 - python
---

I often see code like this:

    message["To"] = formataddr((name, email))

This looks like it should work, especially since the docstring of `formataddr()`
says that it will return a string value suitable for a `To` or `Cc` header.
However, while it works most of the time, it fails if `name` is a
unicode string containing non-ascii characters. It may look ok if you look
simply read `message["To"]`, but as soon as you convert the message or header to
a byte string, you will see the problem.

    >>> from email.Message import Message
    >>> from email.Utils import formataddr
    >>> msg = Message()
    >>> msg["To"] = formataddr((u"Björn", "bjorn@tillenius.me"))
    >>> msg["To"]
    u'Bj\xf6rn <bjorn@tillenius.me>'
    >>> msg.as_string()
    'To: =?utf-8?b?QmrDtnJuIDxiam9ybkB0aWxsZW5pdXMubWU+?=\n\n'


Most code that will use the `To` address in the example will fail, since there's no visible e-mail address in there. The header should look like this, i.e. only the name itself should be encoded:

    To: =?utf-8?b?QmrDtnJu?= <bjorn@tillenius.me>

I wish Python would handle this better. I usually end up writing a helper
function like this for projects I work on:

    def format_address(name, email):
        email = str(email)
        if not name:
            return email
        name = str(Header(name))
        return formataddr((name, email))
