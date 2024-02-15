---
id: how-vim-handles-tabs
aliases: []
tags:
  - fact
  - evergreen
title: How (neo)vim Handles Tabs
---

```lua
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth= 4
vim.opt.autoindent = true
vim.opt.expandtab = true
```

* **tabstop**: how many spaces a tab counts as
* **softtabstop**:  how many spaces act as a tab when in insert mode, eg, when using backspace
* **shiftwidth**: how much to auto-indent when autoindent = true
* **autoindent**: new lines copy the indent level
* **expandtab**: use spaces instead of tabs

Q: What setting controls new lines copying the indent level?
A: autoindent
<!--ID: 1707101119043-->

Q: How do you indent/unindent while in insert mode?
A: Ctrl-T to indent, Ctrl-D to de-indent
<!--ID: 1707637158643-->
