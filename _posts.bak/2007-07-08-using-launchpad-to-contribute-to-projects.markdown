---
layout: post
title: Using Launchpad to contribute to projects
date: 2007-07-08 10:55:00
tags:
 - bazaar
 - garmin
 - launchpad
---

While modifying [pygarmin](http://pygarmin.sourceforge.net/) to support my Edge 305, I was faced with the problem how to submit my patches to be included in pygarmin; I don't have commit access, so I can't commit the changes myself. One way of doing it is of course to generate a diff, and attach a patch to their patch tracker. That has some problems, though, especially since I want to submit a series of patches. The main problem is how to get people to try out the patches. They would have to apply each patch to their version of the source code, and some patches might not apply cleanly after a while.

So, instead of submitting patches to their patch tracker, I make use of [Launchpad](https://launchpad.net/). It has a nice feature that you can import the project's source code and make it available as a [bazaar](http://bazaar-vcs.org/) branch. By importing the code, I can subscribe to [pygarmin's main branch](https://code.launchpad.net/~vcs-imports/pygarmin/trunk) in Launchpad, and get an e-mail notification when someone commits to the branch. But more importantly, I can now easily create a new branch to add support for my Garmin Edge 305:

    bettan:~> bzr branch lp:pygarmin edge-305
    Branched 82 revision(s).

Now I can hack on pygarmin and keep my changes versioned in bazaar, making it easier to keep my patches up-to-date. If code get commited to the trunk branch, I can simply merge and resolve the conflicts:

    bettan:~/edge-305> bzr merge lp:pygarmin

The next thing I want to do is to publish my changes, so that other people can look at them. I do this by pushing my branch to Launchpad:

    bzr push bzr+ssh://bjornt@bazaar.launchpad.net/~bjornt/pygarmin/edge-305

After doing this, the first time, the branch gets registered in Launchpad automatically, and the branch shows up under "Latest code" on the pygarmin page. People can now look and subscribe to [my branch](https://code.launchpad.net/~bjornt/pygarmin/edge-305) to see what changes I make. They can also choose "Browse code" to [see the code, and see the diff](http://codebrowse.launchpad.net/~bjornt/pygarmin/edge-305/changes) of each revision I commit.

If I want someone to try out my changes, I can tell them to get my branch from Launchpad:

    bzr branch http://bazaar.launchpad.net/~bjornt/pygarmin/edge-305
