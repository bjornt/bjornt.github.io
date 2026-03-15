---
layout: post
title: An LLM wrote 100% of my code
date: 2026-03-15 09:00:00
tags:
 - software-engineering
 - ai
 - llm
---

As many of you, I often see the claim that an LLM, or rather an LLM agent
framework (like Claude Code or GitHub Copilot), wrote 100% of someone's code.

I've always been curious whether this could be true or not. I started playing around
with using LLMs in my daily work as a software engineer at the end of last summer. In
the beginning it was truly a struggle. I used an LLM to write code, but I also had to
spend a lot of time reviewing and refactoring the code it generated. At that time, it
also made simple mistakes, like redefining variables or functions, generating code that
wasn't correct, and so on.

However, even though I didn't feel that I was more productive using an LLM than writing
the code myself, I continued trying to make use of LLMs in my work, trying different models,
different frameworks, learning how to prompt, and so on. I learned a lot, but I've also
seen a great improvement in the agent frameworks that are out there. For example, they can
now connect to an LSP server and run unit tests automatically, so they can verify and fix
their code, before they give it to me to review.

I'm now at a point where for a couple of greenfield projects, I've used an LLM and agent framework
to write 100% of the code. I finally feel that I'm productive with an LLM agent
than without.

I now also know that the claim that an LLM wrote 100% of the code can in fact be true.

## 100% writing code != 100% engineering

It should be pointed out that usually the claim is that the LLM **wrote** 100% of the code.
Writing code is only one part of the engineering process. When using LLMs for software
engineering, it's important to understand what an LLM is great at doing, and what it's
not great at doing.

For example, an LLM is great at generating code quickly. It can write code much faster
than any human out there. However, it's not great at keeping a large codebase maintainable.
At least not without guidance from a human software engineer.

An LLM is great when the instructions are clear, and there are already well-known solutions
to the problems. They are great at inferring complicated patterns, but they often fail to
understand subtle nuances. A great example of that is the "Car wash" problem, which proves
to be challenging to understand for an LLM. It basically goes like this:

```
You: I need to wash my car. The car wash is 300 meters away. Should I drive or walk there?
LLM: Walk
```

The LLM focuses on the most common problem, driving or walking, but fails to understand the
nuance that the car needs to get to the car wash somehow. Even frontier models like Claude
Opus 4.6 get this wrong. I tested it today, and it got it slightly better, but still failed:
```
That's a fun little dilemma! For 300 meters, I'd say walk — that's only about a 3–4 minute stroll. Driving such a short distance barely warms up the engine and uses fuel for no real benefit.

That said, if you need to drive the car through an automatic car wash (the kind where you stay in the car), then obviously you'd need to drive it there. But if it's a self-service or hand wash place, walking over is the way to go — maybe even enjoy the fresh air on the way.
```

Is this someone that you would trust to make important decisions about your architecture
and codebase?

## Agent feedback loop

I'm not going to go into details here exactly what I'm doing. I might write another blog
post about that in the future. The details are important, but I also don't think there
is a single best way of doing things. I think people need to try out different approaches
and see what works best for them. I did enjoy reading what
[Mitchell Hashimoto wrote](https://mitchellh.com/writing/my-ai-adoption-journey), and I feel
that my story is quite similar.

However, something that I do think is important is that you have a feedback loop with your
LLM agents. It basically goes like this:

{% include diagrams/feedback-loop.svg %}

Now, let's go through each step in more detail.

## Step 1: Plan

This is where you, as a software engineer, make the architectural decisions and create
a plan for the LLM agent to follow. The better plan you make, the better the LLM agent
will perform.

This step doesn't have to be completely manual. You can make use of an LLM agent to help
you create the plan. The important thing is that the plan is something that you take
accountability for. You are the one that is creating the plan, even if you get help from
an LLM agent.

## Step 2: Delegate

When you have a plan, you can give it to an LLM agent to execute. Again, I'm not going to
go into details here, because there are many ways of doing this. For example, most likely
you will divide up the plan into smaller tasks, and give the LLM agent one task at a time.

For each task, you can also have a feedback loop, so that you can give course corrections
early if you see that things don't go the way you expected.


## Step 3: Review

This is probably the most important step. It's now that you verify that the LLM agent
wrote the code in the way that you expected. Remember that you are the software engineer.
You understand what the code needs to look like in order to keep the codebase maintainable
and scalable.

This is where I currently spend the most amount of time. I go through the code carefully,
and make sure that it matches what I would have written myself. Sometimes it's the LLM agent
that did something unexpected. Sometimes it's the plan that is lacking in details. But
sometimes it could be that I only now realize that the code should be structured differently.

It's also not about code structure and architecture. It includes running the code to make
sure it works, do a security review of the code, checking for subtle bugs, and so on.

Remember, you can still use an LLM agent at this step as well. For me, it helps me produce
better quality code, since doing large refactorings before I submit a PR is much easier than
it used to be.

The goal of the feedback loop is to reduce the amount of time you spend here.

## Step 4: Refine

This is how you reduce the amount of time you spend in Step 3. You need to look at what
you needed to do in Step 3 and try to improve things so that the LLM agent can do a better
job in the future.

Again, I'm not going into details here, since there are many ways of doing this, and it
might depend on whether you use Claude Code, Codex, GitHub Copilot, or something else.

But you should be aware of how your LLM agent gets the context it needs in order to perform
its task. I will give some examples here.

### Prompt

The prompt is the most obvious one, since it's usually how you tell the LLM agent what to do.
You should think about how you write the prompt, but since this is something that you need
to do for every feedback loop, it's one of the least scalable solutions.

### PLAN.md

For larger tasks, it's often helpful to create a document that contains the plan, with the
general outline what needs to be done. But it can also contain example code, breakdowns of
the task into subtasks, links to relevant documentation, and so on.

Take some time to reflect on whether your `PLAN.md` could have been better.

### AGENTS.md

A lot of LLM agents automatically read `AGENTS.md` if it exists for your project. This is
a great place to put project-specific instructions. For example, if you see that the
LLM agent added a lot of useless comments all over the place, `AGENTS.md` is a great
place to add a note that comments should be added only to explain non-obvious code.

As long as the rules make sense on a project level, this is a good place to put them.


### Skills

Modifying `AGENTS.md` is not always the answer, since you need approval from other
team members. For rules that don't have a team-wide consensus, you can create personal
prompt files. Something that automatically gets included in every prompt you write.

There are again many ways of doing this, [agent skills](https://agentskills.io/home) is one
example. Some LLM agents support it, some don't.

The idea is that you can create a library that guides the LLM agent for specific tasks.

In the case of agent skills, they can either live locally
on your filesystem only, or be included in the project repository, as a complement to
`AGENTS.md`.

### Documentation

Another way of guiding the LLM agent is to make sure that your code and architecture
are well-documented. LLM agents usually can read documentation when they need to get
more context, and you can also reference the specific documentation in your plan.

This is something that helps both LLM agents and humans to understand your codebase.

## Vibecoding

When talking about an LLM writing 100% of the code, it's hard to not think about
vibecoding. I see a lot of people talking about it, and I also feel that some
people don't really understand what it means.

What I talk about in this post is not vibecoding. Vibecoding is a term
[coined by Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383).
Basically, they define it as using LLMs to write code, where you trust the LLM
to produce the correct code. You give the responsibility of maintaining the codebase
to an LLM agent.

If you've read this far, it should be clear that what I've been talking about in this
post is not vibecoding. I'm not yet convinced that an LLM agent can maintain a large
codebase in the long term, at least not currently. The LLM agents and models do improve
rapidly, but I still feel that they have a long way to go in this area.

### Vibe coding vs agentic coding

Agentic coding is basically when you move away from using the LLM models through
a basic chat interface. Instead you use something like Claude Code that has agents
that can look at your codebase, talk to LSP language servers, run unit tests, and
even interact with other agents.

Agent engineering has improved the quality of the state of code, but it's not
really related to vibecoding. Even if you use agent engineering, you can still
choose whether you do vibecoding, where you trust the LLM agents fully. Or you
can choose to not do vibecoding, and instead take ownership of the codebase yourself.

### Is vibecoding always bad?

Of course not! Let's say that you're writing a one-off script, doing a functional
prototype to show off some workflow, or small projects that you don't anticipate
will be maintained over time.

In that case, vibecoding can be a great accelerator, since you will save a lot
of time compared to writing it manually, or carefully reviewing the code.
