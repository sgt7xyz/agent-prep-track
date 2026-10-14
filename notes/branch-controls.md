# Why each control exists

_Draft written with Claude's help. Edit it into your own words. The plan's point is that if you cannot justify a control, you will drop it under deadline pressure._

## Required pull request before merging
Every change, whether a person or an agent wrote it, has to appear as a diff that someone reads before it reaches `main`. This is the human checkpoint over machine-written code, the same idea as change management on a production system.

## No direct pushes to `main`
A rule that the owner can bypass is only a suggestion. Turning on enforcement for administrators closed the gap that let my own test push land on `main`, and the test is how I found it.

## Squash merges only
Each pull request becomes one commit on `main`, so the history reads as one reviewed change per line. It also hides messy work-in-progress commits from the record.

## CODEOWNERS
It names who must review which paths, so a change cannot reach `main` without the right person looking at it. On a solo repo it is small, but the file is already in place for when a second person joins.

## Pull request template
The template makes the author, human or agent, answer the same questions every time: what changed, what the agent decided on its own, how it was verified and what risk it carries. An agent tends to hide its own scope creep, and the template drags it into the open.

## Conventional commits
A fixed `type: description` format keeps the log readable by people and by tools. It also makes it easy to see at a glance whether a change was a feature, a fix, docs or a CI change.

## What I learned from testing the controls
A control that is configured is not the same as a control that works. My first protected `main` still accepted a direct push because administrators were exempt, and only an actual test showed it. The same lesson applied to the PR template, which did not appear until it existed on `main`.

## Still to add
Required status checks. There is no CI yet, so there is nothing to require. Session 5 adds it.
