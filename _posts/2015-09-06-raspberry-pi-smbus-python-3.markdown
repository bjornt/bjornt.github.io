---
layout: post
title: Using smbus with Python 3 on a Raspberry Pi
date: 2015-09-06 15:50:00
tags:
 - python
 - orange-matchbox
---

A while ago I got an Orange Matchbox, which is a
[Raspberry Pi](https://www.raspberrypi.org/) running
[Snappy Ubuntu Core](https://developer.ubuntu.com/en/snappy/) together
with an Ubuntu branded case and a
[PiGlow](https://shop.pimoroni.com/products/piglow). The 
[Snappy image for Raspberry Pi](http://people.canonical.com/~platform/snappy/raspberrypi2/)
recently got support for `I2C`, so I tried to drive
the PiGlow using Python 3. It turned out it wasn't trivial, since
`python-smbus` doesn't support Python 3 out of the box. Further more, you
can't install `.debs` in Snappy, so installing `python-smbus` for Python 2
doesn't work either. And it's a C extension, so you can't just copy
over the sources.

I've seen some posts about how you can patch the `python-smbus` source
code and recompile it for Python 3. That's a lot of work when you just
want to try and play around a bit. I instead took a stab at
reimplementing `python-smbus` in pure Python. You can find the result
here:

    https://github.com/bjornt/pysmbus

It only implements two methods so far, `read_byte_data` and
`write_byte_data`, but that goes a long way. I also patched the
[PyGlow](https://github.com/benleb/PyGlow) package to support Python3
and not to require `RPi.GPIO`, which also is a
C extension I don't want to recompile:

    https://github.com/bjornt/PyGlow/

With these two packages, we can now drive the PiGlow using Python 3 in
Snappy Ubuntu Core. First we assemble the code on our desktop machine
and copy it to the Raspberry Pi:

    desktop:~> git clone https://github.com/bjornt/PyGlow/
    desktop:~> cd PyGlow
    desktop:~/PyGlow> wget https://github.com/bjornt/pysmbus/raw/master/smbus.py
    desktop:~/PyGlow> scp -r ../PyGlow ubuntu@pi2:

Then, on the Raspberry Pi, we run the bin_block.py example. Note that we
have to use sudo, so that we get permission to access the I2C bus:

    desktop:~/PyGlow> ssh ubuntu@pi2
    (RaspberryPi2)ubuntu@localhost:~$ cd PyGlow
    (RaspberryPi2)ubuntu@localhost:~/PyGlow$
    (RaspberryPi2)ubuntu@localhost:~/PyGlow$ sudo PYTHONPATH=. python3 examples/bin_clock.py
     Hour | Minute | Second
    01111 | 011001 | 111010 (15:25:58)

If we look at our Raspberry Pi, we should see the PiGlow's lights working:

![PiGlow glowing](/assets/images/orange-matchbox-lights.jpg)
