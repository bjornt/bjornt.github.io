---
layout: post
title: "Dealing with USBError: No Error"
date: 2008-07-29 21:30:06
tags:
 - python
---

In [PyGarmin](http://pygarmin.org/), I used [PyUSB](http://pyusb.berlios.de/) to implement USB support, and I was struck with one odd error. Sometimes, a <code>USBError</code> was raised, with the error message "No error". I couldn't find any documentation for this, and I still don't understand why an error was raised, saying that there was no error.

The error happenend when trying to read from the bus for the first time, after trying to send two packet without any errors. After some testing, I found out that simply trying to read again from the bus didn't work, but if I send the two packets again, everything works without any errors.

For those interested, I fixed this in [revision 91 of PyGarmin](http://bazaar.launchpad.net/~pygarmin-dev/pygarmin/trunk/revision/91).
