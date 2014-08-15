---
layout: post
title: First release of GarminSync
date: 2007-07-14 20:26:15
tags:
 - garmin
 - garmin-sync
 - linux
 - python
---

I have been working on a program that can download data from my Garmin Edge 305 GPS in Linux, and now I've finally got something that's work. The program is called [GarminSync](https://launchpad.net/garmin-sync), and you can [download it from Launchpad](https://launchpad.net/garmin-sync/+download).

Please try it out, but don't expect too much from it. My main focus has been to get something working, now I'm going to focus more on getting it somewhat stable. There are a tons of bugs, for example it sometimes doesn't work to download the data, and you have to simply try to run it again, and/or reconnect the GPS. But at least it's able to download the runs from my GPS and export them to TCX files. It should be possible to such files to [MotionBased](http://motionbased.com/), but it seems like the format is slightly wrong. At the moment I can't get the GPS to work in VMWare, so I haven't been able to get a correct file to compare with.

GarminSync is written in Python, so it probably works on other platforms than Linux as well, but I haven't tried yet.
