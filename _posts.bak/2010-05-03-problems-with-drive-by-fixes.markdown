---
layout: post
title: Problems with drive-by fixes
date: 2010-05-03 12:10:47
tags:
 - launchpad
 - bazaar
---

To start with, I think drive-by fixes are great. If you see that 
something is wrong when fixing something else, it can be a good idea to
fix it right away, since otherwise you probably won't do it.

However, even when doing drive-by fixes, I still think that **each
landed branch should focus on one thing only.** As soon as you start to
group unrelated things together, you make more work for others. It might
be easier for you, but think about all the people that are going to look
at your changes. Please, don't be lazy! It doesn't take much work to
extract the drive-by fix into a separate branch, and most importantly to
land it separately. If you do find that it's too time-consuming to do this, let's talk, and see what is taking time. There should be something we can do to make it easier.

**There's no such thing as a risk-free drive-by fix.** There's always the
potential of something going wrong (even if the application is 
well-tested). When something goes wrong, someone needs to go back and 
look at what was done. Now, if you land the drive-by fix together with 
unrelated (or even related) changes, you basically hide it. By reducing
your workload slightly, you create much more work for someone else.

For example, on Friday I saw that we had some problems with scripts in 
`Launchpad <https://launchpad.net>`_. They were trying to write to a mail directory, to which they
didn't have access. That was odd, since scripts have always talked to 
the SMTP servers directly, and didn't use the queued mailer that needed
write access to that directory. Looking through the recent commit logs 
didn't reveal anything. Luckily enough, William Grant pointed out that 
`r9205 of db-devel
<http://bazaar.launchpad.net/~launchpad-pqm/launchpad/db-devel/revision/9205>`_
contained a change to `sendmail.py`, which probably was the cause of the
problems. This turned out to be correct, but it was still pretty much 
impossible to see why that change was made. I decided that the best thing
to do was to revert the change, but I wasn't sure exactly what to 
revert. That diff of that revision is more than 4000 lines, and more 
than 70 files were changed. So how can I know which other files were 
change to accommodate the change in `sendmail.py`. I tried looking at 
the commit logs, but that didn't reveal much. The only thing I could do 
was to revert the change in `sendmail.py` and send it off to ec2, 
waiting three hours to see if anything broke.

So, I plead again, if you do drive-by fixes (and you should), **please
spend a few minutes extra, to extract the fix into a separate branch, 
and land it separately!**

Is there maybe anything we can do to make this easier to do?
