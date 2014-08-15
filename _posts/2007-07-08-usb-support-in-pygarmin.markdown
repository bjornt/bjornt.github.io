---
layout: post
title: USB support in pygarmin
date: 2007-07-08 11:51:27
tags:
 - garmin
 - python
---

While extending [pygarmin](http://pygarmin.sourceforge.net) to support my Garmin Edge 305, I ran into a problem; pygarmin uses the serial protocol, and some packets that the Edge sends are too big for the serial protocol to handle. So when you request some information from the GPS, you don't get any response back. The solution to this was to add native USB support to pygarmin, making it possible to use the USB protocol to talk to the GPS.

This turned out to be a quite fun task, actually, [pyusb](http://pyusb.berlios.de) makes it easy to communicate to USB devices using Python. Of course it wasn't entirely trivial, since the Garmin protocol specification seems to be out of date, so not everything the Edge 305 does is documented. But last night I finally managed to get something working, I can now specify `"usb:"` as the device to use, so that the USB protocol will be used instead of the serial one. It actually seems to work quite well, although there are some bugs still.

For those of you brave enough, I'd love to get feedback whether it works for you, especially if you have some other Garmin GPS than the Edge 305. You can test it by getting [my edge-305 branch](https://code.launchpad.net/~bjornt/pygarmin/edge-305) of pygarmin and try the following (which should write out some information about your GPS):

`./pygarmin -p "usb:"`
