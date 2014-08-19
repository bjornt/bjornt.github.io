---
layout: post
title: Enabling middleclick scrolling in Ubuntu for Lenovo clickpads
date: 2014-08-19 08:30:00
tags:
 - ubuntu
 - canonical
---

The short version is that if you want to enable middleclick scrolling
for Lenovo clickpads in Ubuntu, do this in a terminal:

    sudo add-apt-repository ppa:bjornt/evdev
    sudo apt-get update
    sudo apt-get dist-upgrade

The commands above should upgrade the `xserver-xorg-input-evdev` package,
as well as remove the `xserver-xorg-input-synaptics` and
`xserver-xorg-input-all` packages.

Next you need to create a file at
`/usr/share/X11/xorg.conf.d/90-clickpad.conf` with the following contents:

    Section "InputClass"
        Identifier "Clickpad"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "evdev"
        # Synaptics options come here.
        Option "Clickpad" "true"
        option "EmulatedMidButtonTime" "0"
        Option "SoftButtonAreas" "65% 0 0 40% 42% 65% 0 40%"
        Option "AreaBottomEdge" "0%"
    EndSection

    Section "InputClass"
        Identifier   "TrackPoint"
        MatchProduct "TrackPoint"
        MatchDriver  "evdev"
        Option       "EmulateWheel"       "1"
        Option       "EmulateWheelButton" "2"
        Option       "XAxisMapping"       "6 7"
    EndSection

The interesting options are `SoftButtonAreas` and `AreaBottomEdge`.
`SoftButtonAreas` specifies where the buttons should be. If you want the
buttons at the top, itt should generally be in the form `"R 0 0 H L R 0 H"`,
where `R` is where the border between the middle and right buttons, `H`
is the height of the buttons, and `L` is the border between the middle and
left buttons.

The `AreaBottomEdge` turns off the touchpad, expect for clicking. If you
want to keep using the touchpad, you can instead specify `AreaTopEdge`,
with the same value you use for `H`. That would enable the touchpad below
the buttons.

Unfortunately, you can't specify where the left button should be,
instead if occupies everything that isn't the middle or right button.
This is a bit annoying, since at least I tend to touch the touchpad with
my palm when reaching for the middle button, which will result in a left
click being registered instead of a middle click.

I created this package because Ubuntu doesn't quite support the
clickpads that come in the newer Lenovo laptops. Ubuntu does support
clickpads, and with the `SoftButtonAreas` config settings it's possible to
have three soft buttons on the clickpad where the real buttons used to
be. However, what's not supported out of the box is middleclick
scrolling, where you hold the middle button and scroll with the
trackpoint.

The main problem is that the clickpad is driven by `synaptics` and
the trackpoint by `evdev`, and they can't communicate to generate the
scroll events. Bae Taegil [patched the `evdev` driver](https://aur.archlinux.org/packages/xf86-input-evdev-trackpoint/) to basically include
the `synaptics` driver. I've taken that patch and generated a package for
Ubuntu 14.04. I've only added a package for Trusty, but I could add packages
for other releases if needed. I will most likely add one for Utopic,
when it becomes more stable.
