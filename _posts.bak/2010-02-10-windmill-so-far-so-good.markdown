---
layout: post
title: Windmill - so far, so good
date: 2010-02-10 12:51:17
tags:
 - launchpad,
 - python,
 - windmill,
 - testing
---

We've used Windmill in our Launchpad buildbots for a while now, and it's actually
worked out quite well. I was afraid that we would have a lot of fallout,
since in the beginning Windmill was fragile and caused a lot of
intermittent test failure. However, so far I'd said that we've had very
little problems. There was one intermittent failure, but it was known
from the beginning that it would fail eventually. Apart from that we've
had only one major issue, and that's that something is using 100% CPU
when our combined Javascript file is bigger than 512 000 bytes. This
stopped people from landing Javascript additions for a while, and we
still haven't resolved this issue, apart from making the file smaller.

There are some things that would be nice to improve with regards to
Windmill. The most important thing is to make sure that launchpad.js can
be bigger than 512 000 bytes:

 * <https://launchpad.net/bugs/519744>

It would also be nice to make the test output nicer. At the moment
Windmill logs quite a lot to stderr, making it look like the test
failed, even though it didn't. We don't want Windmill to log anything
really, unless it's a critical failure:

 * <https://launchpad.net/bugs/494519>

I was going to say that we also have some problems related to logging in
(because we look at a possibly stale page to decide whether the user is
logged in), but it seems like Salgado already fixed it!

 * <https://launchpad.net/bugs/515494>

It would also be nice to investigate whether the problem with asserting
a node directly after waiting for it sometimes fails. We had problems
like that before; code was waiting for an element, and when using
assertNode directly after the wait, the node still didn't exist. I
haven't seen any test fail like that lately, so it might have been fixed
somehow:

 * <https://launchpad.net/bugs/487666>

There are some other things I could think of that would be nice to have.
I haven't found any bugs filed for them, but I'll list them here.

 * Don't run the whole test suite under xvfb-run. It'd be better to   start xvfb only for the Windmill tests.
 * Use xvfb by default for Windmill tests. When running the Windmill      tests it's quite annoying to have Firefox pop up now and then. It'd      be better to run them headless by default.
 * Switches for making debugging easier. Currently we shut down      Firefox after running the Windmill tests. It should be possible to      have Firefox remain running after the test has finished running, so that you can manually poke around if you want to. If we use xvfb by default, we also need a switch for not using it.
