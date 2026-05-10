---
layout: post
title: Writing an AI Agent
date: 2026-05-10 16:55:00
tags:
 - software-engineering
 - ai
 - llm
---

I recently created [maas-code-reviewer](https://github.com/canonical/maas-code-reviewer), which is
an AI agent that reviews code for the MAAS team at Canonical. While doing so, I learned a few things
that I think are worth sharing.

It's actually quite easy to write an agent. But it's also quite easy to write an agent that eventually will expose your secrets or delete your data.

If you understand how an agent works, it's not too hard to make sure that your agent is secure and won't do any harm.

The purpose of this blog post is to help you understand how an agent works and what security aspects you need to consider.

## TL;DR

If you don't have time to read the full post, the most important takeaways are:

- Make use of the LLM as little as possible
- Give the LLM access to tools so that it can get more context and verify its work
- Don't expose any secrets to the LLM
- Sandbox the LLM - especially the tools

## What is an AI agent?

When I talk about an AI agent, I mean a system that uses an LLM to perform a task autonomously.
There are many ways of writing an AI agent. For example, you can extend an existing agent harness like Claude Code
or GitHub Copilot.

For my AI agent, I chose to write it from scratch, using Python and `google-genai`. That gives me full control
and makes it easier to understand how the agent works.

## Architecture

The code review agent that I wrote has a few different parts:

- Check for new PRs
- Get PR details
- Get code details
- **Review the code**
- Post review to the PR

Only one of those parts, **Review the code**, actually uses the LLM. Everything else is written in Python or handled by a GitHub workflow.

{% include diagrams/agent-workflow.svg %}

## LLM context handling

The only part that uses the LLM is the **Review the code** part. Let's take a closer look at that.

In order for the LLM to do its work, it needs context. That's how it works: it gets input tokens/context and generates output tokens, the actual text or code.

For a code review there are a few things that we know that we need:

- System prompt
- Diff
- PR description

But then there are a few other things that may, or may not, be needed. These are things like:

- Get file contents
- Validate JSON
- Get line number

{% include diagrams/llm-context.svg %}

### Always-provided context - prompt

The always-provided context is basically what you would give to an LLM as a prompt in a chat interface. You tell it what to do, and then you might attach some files for more context.

That's exactly what we're doing here. We have a system prompt, which tells the LLM that it's a code reviewer and it should do a code review. We can fine-tune the system prompt in order to have it focus on different aspects of a code review.

Then, of course, the LLM needs the diff, so that it can actually do the review. We also include the description from the PR, so that the user has a way of justifying the code changes.

### On-demand context - tools

While having only the automatically provided context can produce decent results, it's when you allow your agent to fetch context on-demand that you see it producing excellent results. We simply can't predict exactly what context might be needed. For example, yes, we could already include the contents of each file that's touched by the PR. But for large mechanical changes, that might increase the context too much, and might not help. In fact, providing too much context can actually make things worse.

Instead we let the LLM decide whether it needs more context. The way we do that is by providing tools to the LLM. Now, there are other ways, like Agent Skills and MCP, but under the hood they are implemented using the tool-calling functionality of the LLM or require specific support in the agent harness. Note that not all models support tool calling. Choose one that does, if you need it.

Tools allow two important functions for the LLM. The first one is to **get more context**, like getting the contents of a file. But tools can also **help the LLM validate its work**. 

#### Context getters

For the code review agent we have two tools that can get more context. One is to list the files in the repository, so that it can see which files are available. The other tool is to read the file contents, so that the LLM can bring in more code context, or read AGENTS.md to get more guidance on how to do the review and understand the code.

#### Validators/helpers

You may have noticed that during the last 6 months or so the coding harnesses have become much better and stopped making stupid mistakes like defining duplicate functions. A big reason for that is that the tools have become better. After the LLM has generated some code, it can now use tools to validate that what it did was actually correct. If you look at the thinking output of a model, which I would encourage you to do, you often see that it first produces something, then realizes that what it produced didn't work, and then it fixes itself automatically. Of course, part of the improvements are due to the models, and especially the reasoning, becoming better, but the tools are also a big part of it.

For the code review agent we have two validators/helpers. The first one is **Validate JSON**. In the system prompt we ask the LLM to produce structured JSON so that we can then use that to post to GitHub or Launchpad, or even generate markdown for local consumption. Since the LLM may make mistakes, we let it validate its output, so that it can fix it automatically.

The second tool is one that helps it find the right line number in the file. We want it to comment on the code with the line number as context, so that we can add inline comments in a GitHub PR. The LLM can get the line number from the diff, but since LLMs are usually bad at counting, it's better to provide a tool for that.

## LLMs are unpredictable

There's a reason I chose to limit the LLM usage to only the part that I can't code in Python, or any other language.

LLMs are unpredictable. They are not deterministic by default. If you give an LLM the same prompt twice, it's very likely that you will get two slightly different answers. Yes, you can make LLMs more likely to produce the same output by lowering the temperature of your model, but that only works if your input context is fixed. And even then, it's not as simple as that. You basically have no guarantee of getting a deterministic behavior from an LLM. In the case of a code review, we have to inject user-generated context into our prompt, which makes it even harder to control the end result.

Sure, you can mitigate some of this by dividing your agent into smaller parts, each with their own context. But again, if the model provider decides to tweak their weights, you will get different results.

My advice is to **only use the LLM for the parts which don't have clear rules and logic**. If the logic is deterministic, tell the LLM to write code for you instead. That way you can see what actually happens, and if there's a problem it will be much easier to debug.

## LLMs are insecure

When you're using an LLM, you should keep these things in mind.

- If an LLM has access to your secrets, it will eventually expose them
- If an LLM has the ability to delete your data, it will eventually delete your data

You've probably seen reports that secrets have been exposed by an LLM, or an LLM deleted the production database, even though it was told not to do it?

The main problem here is that the LLM had the possibility of doing that in the first place. Given that an LLM is not deterministic, it doesn't matter how many guardrails you put in your prompt. Given enough time, the LLM will do it anyway. I would consider anything that you put in a prompt, even when written as a structured markdown document, the way agent skills and similar systems expect you to define guardrails, to be more of a guideline than a guardrail.

That's why, when using an LLM, you should never give it access to any secret, or the ability to delete any data that you wouldn't be able to recover if needed.

When it comes to restricting the LLM, the always-provided context is easy. You control how you generate it, so you can ensure that no secrets are included.

### Prompt injection

While not including any secrets or allowing access to sensitive data is the right approach, it's also worth talking about prompt injection.

All the context together basically forms a big prompt. In our case, the PR description, the diff, and the files in the repo are all places where the user can inject a prompt.

Prompt injection is hard to protect against. You can have a sentence like `Never read ~/.ssh/id_rsa` in your prompt, but with the right technique someone can craft a PR description that makes the LLM ignore that guideline.

So, while you might not be able to prevent prompt injection, you should be aware of it. In the case of a code review agent, this means you shouldn't use it to automatically merge and deploy code just because the agent approved it.

Rather, when prompt injection is possible, you should treat the agent's output as a guideline only. Something else, most likely a human reviewer, should have the final say.

### Securing your tools

The tools that you provide to the LLM require more consideration. You need to make sure that they run inside a sandbox.

For example, we have a tool for reading a file. If we simply allow it to read any path, it could easily read any file on your filesystem, including secrets that you have in a parent directory. That's why, in the tool implementation, there are specific checks that the resolved paths (to handle symlinks) that the LLM wants to read are inside the git repository we want to review. So it can read any file inside the git repository, but if it tries to read any other file, it will be refused.

And while this code review agent doesn't have a tool that runs arbitrary commands, that's a type of tool that needs extra consideration. Securing such a tool is very hard. For example, if the LLM can execute any command, it could execute `cat ~/your-secret-file`. Or, if you have a secret in an environment variable, it could execute `env`.

This is the reason most coding harnesses require you to confirm each tool usage. The other way is to sandbox your execution environment. For example, you could execute the command inside a container, which doesn't have any secrets. And if the LLM does execute `rm -rf /`, you can easily re-create the container.

## Wrapping up

I hope that you now know more about writing an AI agent and that you now can write a secure one without any problems.

Use the LLM only for the parts that genuinely need it, give it tools to make it work better, and assume that any secret it has access to eventually will be exposed. In other words, don't give it any secrets, unless it doesn't have any way of publishing those.

If you'd like to see what this looks like in practice, the full code for the agent is at [maas-code-reviewer](https://github.com/canonical/maas-code-reviewer).
