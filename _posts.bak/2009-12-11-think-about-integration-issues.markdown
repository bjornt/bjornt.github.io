---
layout: post
title: Think about integration issues
date: 2009-12-11 16:35:12
tags:
 - python
 - launchpad
---

When doing work on something that is supposed to be used by others, don't forget to think about how it's actually going to be used. Not
only to think about it, but to actually try it out, to confirm that it
works nicely when integrated, and that it's easy to integrate
it. And let's not forget to document how to integrate it, and ideally to
test it as well.

As an example, in [Launchpad](https://launchpad.net/launchpad) we use 
[lazr-js](https://launchpad.net/lazr-js) for our Javascript 
infrastructure. We recently changed the way it's integrated into 
Launchpad, giving it a proper `setup.py` file, so that we can generate 
an egg and depend on it through [Buildout](http://buildout.org/). The 
integration issue was of course taken into account there, making sure it
was easy to build lazr-js both standalone, and when used in another 
project, like Launchpad. There was one command to build everything, 
which is simple enough. However, one thing wasn't done. It wasn't 
documented how you should use lazr-js in another project. Therefore,
when people continued to develop lazr-js, adding more features, and
making the build system more complicated, there wasn't much thought 
about keeping it easy to build lazr-js in other projects. The build 
process became more complicated, multiple commands had to be executed.
This is fine when building lazr-js by itself, since all you have to do 
is `make build`. However, when using lazr-js as an egg, you don't have 
access the `Makefile`, which means that you have to duplicate the build
steps. Therefore, having the build to be more than one command, makes it
harder to use elsewhere. In fact, the build process of lazr-js 
changed so much, that we didn't know anymore, how to properly use the 
latest version of lazr-js in Launchpad.

This is just one example of integrating external libraries. But the same
is true for code internal to the project. When developing code that is 
to be used by multiple call sites, it's important to think about how 
it's actually going to be used. It's easy to get carried away, 
developing a, what you think, really nice API. But then when people 
start to use it, it turns out that it's not so nice.

**What can be done to avoid integration issue?** Ideally, you should 
document and test how the integration is supposed to work. By doing this,
you get a feel of how to use the API. Doctests are actually quite nice 
for this purpose. If you manage to produce a readable doctest, it's 
quite probable that your API is easy enough to use.

Sometimes adding tests for integration isn't feasible. For example,
in the case of lazr-js is not that easy. What I do when I develop on 
lazr-js is to have a throw-away Launchpad branch, where I use my lazr-js
branch and manually make sure that it works nicely when integrated. Take a look at how it looks when integrated. What steps do you have to do to use it? Is that something that you will want to do for every call site? Are people likely to copy and paste an existing example to use your code? If the answer to the last question is yes, it's not easy to use your code.
