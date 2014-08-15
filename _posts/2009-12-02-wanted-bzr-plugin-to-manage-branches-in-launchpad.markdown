---
layout: post
title: "Wanted: bzr plugin to manage branches in Launchpad"
date: 2009-12-02 12:20:16
tags:
 - bazaar
 - launchpad
 - launchpadlib
---

I will probably implement this myself at some point, but if anyone wants to use their [bzr](http://bazaar-vcs.org/) and [launchpadlib](https://launchpad.net/launchpadlib) skills to make the world a slightly better place, I'd be grateful. You don't even have to have any bzr and launchpadlib skills, both are quite easy to get started with. This could be a great opportunity to learn more about them!

I want a [bzr plugin](http://bazaar-vcs.org/WritingPlugins) that queries [Launchpad](https://launchpad.net/) and list all my branches that aren't `Merged` or `Abandoned`. I want it to work in the context of a branch, so that it automatically knows which project I'm interested in, although having it work outside a branch and list branches for all my projects would be useful as well.

To remove branches from the list of active branches, I'd also like to be able to mark a branch as `Abandoned` using the plugin.

Bonus points if any attached merge proposals and their status also are listed.
