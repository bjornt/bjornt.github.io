---
layout: post
title: Technical Architect Roadmap
date: 2010-02-24 12:12:23
tags:
 - launchpad
---

I made the transition from the Bugs team lead to the Launchpad Technical Architect quite a
while ago. While the first time was spent mainly on satisfying my
coding desires, it's time to define what I'm going to spend my time as
technical architect! My road map that shows the high level things that
I'll be focusing on is available here:

  * <https://dev.launchpad.net/TechnicalArchitect>

I'll also be writing blog posts (and sending mails to the launchpad-dev
mailing list of course) regularly to keep people updated with my
progress and findings. My blog is at <http://tillenius.me/> and I tag all
posts related to Launchpad with [`launchpad`](http://tillenius.me/blog/tag/launchpad/).

I'm currently working on [decoupling our feature development cycles with
our release cycles](https://dev.launchpad.net/LEP/ReleaseFeaturesWhenTheyAreDone), which I do mainly, because I think it's important, not because it's part of the technical architect's responsibility.
But in parallel with that my next task is to set up a team that can help
me doing a good job. I'll expand more about the team in another post,
but in short it will consist of members from each sub-team in Launchpad.
It will act as a forum to discuss what needs my attention, and they will
also help me figuring out solutions to problems, and help me implement
the solutions.

One of the first major tasks will be to come up with a testing strategy.
Currently when we write tests we don't think that much about it.
Everyone have their preferences, and we have a wide variety of testing
styles, making it hard to find which code paths are exercised by which
tests, and how good test coverage we have. This leads to us sometimes having
bad test coverage, and some times having too much test
coverage, i.e. we have redundant tests that make the test suite slower.
Coming up with guidelines on how to write tests, which kind of tests to
write, where to place them, etc., is the first step. But we also need to
figure out how to make our test suite faster, what kind of documentation to 
provide, and so on.

In addition to the tasks on the roadmap, I also have a number of things I do on a regular basis. This includes reviewing database patches for API consistency, help teams design features from a technical point of view, keep my eyes open for areas in the code that need refactoring and clean-up.
