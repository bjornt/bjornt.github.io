---
layout: post
title: VLAN tagging with Linksys E8350
date: 2015-05-31 14:00:00
tags:
 - vlan
---

I bought a [Linksys E8350](http://www.linksys.com/us/p/P-E8350/) router to
replace the router my ISP gave me as well as an old Linksys WRT610N router.  I
chose the E8350, since from the setup screenshots it looked like it could do
VLAN tagging, which I need. I was disappointed at first, since the UI doesn't
allow you to do VLAN tagging for the LAN ports. But it turned out that with a
little bit of hacking, it's possible to do it.

Doing VLAN tagging with 5 ports is quite limiting, but just about enough
for my use case. I get a, somewhat odd, trunk from my ISP which has a VLAN
for IPTV traffic, but regular Internet packets aren't tagged. I have the
router in my bedroom and want to access both the LAN and IPTV networks in
my living room. But I have only a single cable connecting the rooms, so I
use VLANs to be able to connect both networks with one cable.

The first attempt to make port 4 the trunk for the IPTV and LAN VLANs
failed:

![Failed VLAN taggging attempt](/assets/images/vlan-fail.png)

It's odd, because the UI looks like it would allow creating a trunk on
the LAN ports. A closer look at the Javascript that does the validation
revealed this:

        for(i=1;i<VLAN_ENTRY;i++)
        {
            obj = getEle(ele_id_name[ele]+i);
            if(obj.value != port_option[2])
            {
                if(flag == true){
                    //[share.js]errmsg.err104="A VLAN port can be untagged to only one VLAN ID.";
                    alert(errmsg.err104);
                    obj.focus();
                    return false;
                }
                flag = true;
            }
        }
        return true;

The commented out error message makes sense. A port can't be untagged in
different VLANs. But the actual code checks also that a port can't be
tagged in different VLANs, and that doesn't make much sense. It could be a
bug, but considering that the actual error message that was displayed
doesn't mention 'untagged', it could be that they took an existing VLAN UI
from some other product, and just crippled it. The E8350 is a consumer
model after all.

Now, what would happen if the validation above would be disabled? The
Javascript is in the HTML file, and Chromium Developer Tool doesn't
allow such Javascript to be edited. Instead, let's put a breakpoint
whenever `flag` is set to `true` and use the Javascript console to set it
back to `false`.

![Successful VLAN taggging attempt](/assets/images/vlan-success.png)

 Look at that, it worked!
