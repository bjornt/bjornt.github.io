---
layout: post
title: Block on test failures
date: 2009-12-21 14:28:25
tags:
 - launchpad
 - python
---

I can't stress enough how important it is to automatically block, stop
the line,  when a regression occurs. Forcing someone to take action.
Don't think it's enough to have tests to catch regressions. It won't
help you much, unless you run them automatically, and most importantly,
block on test failures, forcing someone to fix them.

In Launchpad we have been quite good at this in the past. Already from
the beginning we ran the whole test suite before every commit. If a test
failed, the commit wasn't made, and the committer had to make the test
pass before being able to commit those changes to the mainline. Now we
have something similar. For performance reasons, instead of running the
tests before the commit, we run them after. If a test fail, we enter
*testfix mode*, blocking all commits to mainline, until the test passes
again.

But, when we decided to bring in AJAX into the equation, we failed to do
the same for the new test infrastructure we added. We use Windmill to
test our AJAX functionality, and since it was a bit flaky, and it wasn't
trivial to integrate it into our existing test suite, we thought it was
enough to be able to run the tests manually to avoid regressions. This
was a big mistake. Not many people are going to run the tests manually,
so regressions are bound to sneak in without you noticing it. Believe
me, I know. I integrated the Windmill tests into our normal
`zope.testing` test runner. When I did this, I found out that a lot
of our Windmill tests were actually failing. We set up a buildbot 
builder to run the Windmill automatically, hoping that it would make
regressions less likely to be introduced without us knowing about it. It
helped a bit, we actually did catch a few regressions, but it was hard
manual work. It required someone (me!) to keep an eye on the buildbot
runs, looking through the test log, and chase people to fix it.  This
led to having not all the tests passing most of the time, which made it
even harder to notice new regressions. So while simply having the tests
run automatically helps a bit, it still requires a lot of discipline and
manual work to prevent regressions from being unnoticed.

That's why I'm pleased to announce, that **Windmill tests are now 
included in the regular Launchpad test suite**, which means that when a
Windmill test fails, we will enter *testfix mode* and we're forced to
take action. It will be a bit painful in the beginning. I'm sure that we
will see some spurious test failures. However, I'm sure it will be less
painful that it has been to keep the current Windmill test suite under
control.

The next time you add new testing infrastructure, let's include it in
the regular test suite from the beginning, OK?
