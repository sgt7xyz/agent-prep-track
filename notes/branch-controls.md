# Why Each Control Is Important

## Required Pull Request Before Merging
Every change, whether it's made by me or an AI agent, needs to go through a pull request before being merged into `main`. This gives me a chance to review the changes and make sure everything looks right. It's basically the same concept as change management in a production environment.

## No Direct Pushes to `main`
The whole point of protecting `main` is to prevent anyone from making changes without going through the proper process, including myself. During testing, I discovered that I could still push directly to `main` because administrators were exempt from the rule. I fixed that by enabling enforcement for administrators as well.

## Squash Merges Only
Squash merging combines all the commits from a pull request into a single commit on `main`. This keeps the commit history clean and makes it easier to track what changed. I don't really need every little commit I made while working on something showing up in the main branch.

## CODEOWNERS
The `CODEOWNERS` file identifies who is responsible for reviewing changes to certain files or directories. Right now, I'm the only person working on the repository, so it's pretty straightforward. However, having it in place makes it easier to manage reviews if other people start contributing.

## Pull Request Template
The pull request template makes sure every change includes some basic information, regardless of whether I made it or an AI agent did. It covers what changed, what decisions the agent made on its own, how the changes were tested, and any potential risks.

This is particularly useful with AI agents because they sometimes make changes beyond what was originally requested. Having everything documented makes those changes easier to identify during review.

## Conventional Commits
Conventional commits provide a consistent format for commit messages, such as `feat:`, `fix:`, `docs:`, or `ci:`. This makes the commit history easier to read and helps me quickly identify what type of change was made. It also makes the history easier for automated tools to process.

## What I Learned From Testing the Controls
One of the biggest things I learned is that **just because a security control is configured doesn't mean it's actually working.**

For example, I initially thought `main` was protected, but when I tested it, I was still able to push directly because administrators were exempt. I wouldn't have caught that without actually testing the rule.

I also discovered that the pull request template wouldn't show up until the file was merged into `main`.

The main takeaway for me is that **you need to test your controls instead of assuming they're working just because you enabled them.**

## Still To Add
The next thing I need to implement is required status checks. Right now, I don't have a CI pipeline configured, so there aren't any automated checks to enforce.

I'll be adding CI in Session 5, and once that's working, I can require those checks to pass before allowing a pull request to be merged.
