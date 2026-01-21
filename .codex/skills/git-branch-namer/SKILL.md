---
name: git-branch-namer
description: Create a git branch name using the conventions defined in a source of truth 
metadata:
  short-description: Create git branch name.
---

Source of truth:
- Notion page [git conventions](https://www.notion.so/git-2e2527e3ee64808f8c02f3c59f16df20)


What information to use:
- Inputs data given by yourself or the user (ticket content, ticket reference, current context, ...)
- Conventions in the source of truth
- If ticket id is missing, DO NOT invent it. Ask for it or stop.


Workflow:
1) Read the conventions in the source of truth
2) Given the conventions and the inputs data, create a branch name
3) output the branch name
