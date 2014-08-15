---
layout: post
title: Linux support for Garmin Edge 305
date: 2007-03-24 14:56:15
tags:
 - garmin
 - linux
---

I recently bought a new gadget for my bike, a [Garmin Edge 305](http://www.garmin.com/products/edge305/). It's a GPS-enabled bicycle computer, which tracks your position, speed, pulse, altitude, etc., and you can of course download the data to your computer and analyse it. You can also upload data to it, for example workout programs, courses, and more.

The sad thing is that its Linux support is currently limited. Tools such [gpsbabel](http://www.gpsbabel.org) and [gpsman](http://www.ncc.up.pt/gpsman/) claim to support the device, but I haven't gotten it to work yet. Also, those tools are mainly for extracting GPS data, they don't handle other data, such as pulse and laps that well.

But there is hope! I found a project called [pygarmin](http://sourceforge.net/projects/pygarmin/) which is a Python library for communicating with Garmin GPS devices. The library is based on [Garmin's Device Interface SDK](http://www.garmin.com/support/commProtocol.html), so it shouldn't be too hard to make it support my GPS device. The protocol specification doesn't seem to include all the commands that the Edge uses, but there's an open source tool for Windows, [MotionBased Agent](http://sourceforge.net/projects/motionbased/), which should be able to download and upload data to a Garmin Edge 305, so it should be possible to find out what needs to be added to pygarmin.
