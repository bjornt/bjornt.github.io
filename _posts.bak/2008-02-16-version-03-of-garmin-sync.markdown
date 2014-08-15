---
layout: post
title: Version 0.3 of garmin-sync
date: 2008-02-16 12:44:28
tags:
 - garmin-sync
 - garmin
 - linux
---

It's been a while, but I've finally found some time to work on `pygarmin` and `garmin-sync` again. This has resulted in a new version of `garmin-sync`, 0.3. Not much has changed since 0.2; the biggest changes are in `pygarmin` itself. In general, this version should work better for people who had trouble getting it to work in the past.

You can download it at [https://launchpad.net/garmin-sync/+download](https://launchpad.net/garmin-sync/+download)

New features include:

    * More robust USB communication
    * Possibility to get debug information, to help fix problems
    * Might work with Forerunner (testers needed)
    * Fixed bug 135717 (Missing data point for Forerunner)
    * Fixed bug 154081 (Some value errors when running garminsync.py)

I'm hoping this release will make`garmin-sync` work with the Forerunner series, and not only with Edge. If you have a Forerunner, please give it a try, and tell me whether it works.

If you have problem getting your GPS to work, please run `garmin-sync` with `-d usb.packet` and send the output to me. That will help me debug what's wrong.
