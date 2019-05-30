# Contributing to dazl

Welcome! This document provides a high-level overview of how to contribute to the development of dazl.

(For information on how to build, test, and work on the codebase, see the [README](./README.md).)

There are many ways you can contribute beyond coding. For example, you can report problems, report and clarify issues, and write documentation. If you're completely new to open source, the [Open Source Guides](https://opensource.guide) is a great place to start.

## Code of conduct

This project and everyone participating in it is governed by the [DAML Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [community@digitalasset.com](mailto:community@digitalasset.com).

## Git conventions

For Git commit messages, our principle is that `git log --pretty=oneline` should give readers a clear idea of what has changed and the detailed descriptions should help them understand the rationale. To achieve this:

* Commits must have a concise, imperative title, prefixed with either `python` or `meta` e.g.:
  * *meta: Add legalese (CONTRIBUTING notice, LICENSE, notice).*
  * *python: Improve explanation of …*
  * *python: Remove module X because it is not used.*
* Commits should have a description that concisely explains the rationale and context for the change if that is not obvious.
* Commit descriptions should include a `Fixes #XX` line indicating what GitHub issue number the commit fixes.
* The git logs are not intended for user-facing change logs, but should be a useful reference when writing them.

## Pull request checklist

- Read this document (contribution guidelines).
- Does your PR include appropriate tests?
- Make sure your PR title and description makes it easy for other developers to understand what the contained commits do.
- If your PR corresponds to an issue, add “Fixes #XX” to your pull request description. This will auto-close the corresponding issue when the commit is merged into master and tie the PR to the issue.
- If your PR includes user-facing changes, you must add a line describing the change to the [release notes](docs/source/support/release-notes.rst) as part of your PR.

## Working with issues

We use issues and [pull requests](https://help.github.com/articles/about-pull-requests/) to collaborate and track our work. Anyone is welcome to open an issue. If you just want to ask a question, please ask away on [Stack Overflow](https://stackoverflow.com/questions/tagged/daml) using the tag `daml`.

We encourage everyone to vote on issues that they support or not:

* 👍 - upvote
* 👎 - downvote

When you start working on an issue, we encourage you to tell others about it in an issue comment. If other contributors know that this issue is already being worked on, they might decide to tackle another issue instead.

When you add `TODO` (nice to have) and `FIXME` (should fix) comments in the code, we encourage you to create a corresponding issue and reference it as follows:

* `TODO(#XX): <description>` where `#XX` corresponds to the GitHub issue.
* `FIXME(#XX): <description>` where `#XX` corresponds to the GitHub issue.

### Labels

We use labels to indicate what component the issue relates to (`component/...`). We use some special labels:

- `broken` to indicate that something in the repo is seriously broken and needs to be fixed.
- `discussion` to indicate the issue is to discuss and decide on something.
- `good-first-issue` to indicate that the issue is suitable for those who want to contribute but don't know where to start.

By default, issues represent "work to be done" -- that might be features, improvements, non-critical bug fixes, and so on.

### Milestones

Issues are grouped into *milestones* that correspond to future planned releases of the library. Issues without a milestone are treated as in need of triaging.

The active milestones arse listed [here](https://github.com/DACH-NY/dazl/milestones).

## Discussions

Discussions on this repository should be limited to the dazl library. Discussions more generally about daml or the lower-level language bindings that are formally included in the SDK should be discussed on the [DAML repo](https://github.com/DACH-NY/daml).

# Thank you!

Thank you for taking the time to contribute!
