---
layout: post
title: "RFC: Expose features to users when they are done, not once a month"
date: 2010-03-04 18:56:41
tags:
 - launchpad
---

I've been working on [a new release/merge workflow][0] for Launchpad.
I've written it from the developers' point of view, but I'd love some
comments from users of `launchpad.net`, so let me try to explain how you, as
users, would be affected by this change.

[0]: https://dev.launchpad.net/MergeWorkflowDraft

The proposal is that we would decouple our feature development cycles
from our release cycles. We would more or less get rid of our releases,
and push features to our users when they are ready to be used. Every
feature would first go to `edge.launchpad.net`, and when it's considered
good enough, it will get pushed to `launchpad.net` for everyone to use.
Bug fixes would also go to `edge.launchpad.net` first, and pushed to
`launchpad.net` when they are confirmed to work. Sadly, Launchpad will still go down once a month for updating DB and other regular maintenance, just like before. The amount (and frequency) of downtime would stay the same as before.

There are users who are in our beta team and use `edge.launchpad.net`
all the time, and those who want a more stable Launchpad, and use
`launchpad.net`.

Users of `launchpad.net`
------------------------

Those who aren't in the beta team would get bug fixes sooner than with
the current workflow. Instead of having to wait for the end of the
release cycle, they will get it as soon as the fix has been confirmed to
work on `edge.launchpad.net`. The same is true for features, kind of.
These users would have to wait a bit longer than today, since today we
push even unfinished features to `launchpad.net` users at the end of the
release cycle. With the new workflow, these users would have to wait for
the feature to be considered complete, but in return these user should get
a better experience when seeing the feature for the first time.

One potential source of problem is that even though fixes and features
get tested on `edge.launchpad.net`, before going to `launchpad.net`,
with each update there is the potential of some other issue being introduced. For example, fixing a layout bug on one page, might make another page look different.
With the current workflow this happens only once a month, instead of a
few times every month with the new workflow. That said, even today we
update `launchpad.net` multiple times every month, to fix more serious
issues.


Users of `edge.launchpad.net`
-----------------------------

If you are in the beta team, and use `edge.launchpad.net` on a regular
basis, it won't be that different from how it works today. Just like today, you
would be exposed to features that are under development. What would
change is that we will try to do a better job at telling you which
features that are on `edge.launchpad.net` only. This way you will have a
better chance at actually helping us test and use the features, and
tell us about any problems, so that we can fix it right away. This
should make you more aware of new features that are being added to Launchpad, and provide a better opportunity for you to make it better.

One potential source of problem here is that developers will know that
their work won't end up on `launchpad.net`, before they say it's ready,
so they push more rough features to `edge.launchpad.net`. Thus it could be
a more rockier ride than today. But of course, our developers care a lot 
about their users, so they won't land their work, unless it's really good! :-)

Conclusion
----------

My hope is that this will provide a better and stable experience for users of `launchpad.net`, and provide users of `edge.launchpad.net` a better opportunity to help us making new features rock! But I'm interested to hear what you, the actual users, think about this.
