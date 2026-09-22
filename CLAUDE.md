# CLAUDE.md — Raphael Kit for Raspberry Pi Docs

## Repo layout

- Docs live in `docs/`; sample source code lives in the `master` branch.
- Branch `docs` = English; one branch per language: `docs-de`, `docs-es`, `docs-fr`, `docs-it`, `docs-ja`.
- Each branch is a separate Read the Docs project and builds its own site:
  `docs` → `raphael-kit`, `docs-de` → `raphael-kit-de`, `docs-es` → `raphael-kit-es`, `docs-fr` → `raphael-kit-fr`, `docs-it` → `raphael-kit-it`, `docs-ja` → `raphael-kit-ja`
  (served at `docs.sunfounder.com/projects/raphael-kit/<lang>/latest/`).

## Syncing a change to all languages

- Any change to one language's docs must be applied to all 6 branches (`docs` + 5 language branches).
- Language worktrees are checked out under `.claude/worktrees/<branch>`
  (`git worktree add .claude/worktrees/<branch> <branch>`).
- Text edits: edit in place in each language's own wording (e.g. German「+」mit 5V, French「+」au 5V, Japanese「+」を5Vに) — never copy English sentences into language branches.
- Images: language-independent — copy the same file to the same path in every branch.
- Duplicate image copies (update BOTH, verify with md5):
  - `docs/source/img/image349.png` == `docs/source/python_pi5/img/2.1.6_rotary_encoder_schematic.png`
  - `docs/source/img/list_2.1.3_tilt_switch.png` == `docs/source/python_pi5/img/2.1.5_tilt_switch_list.png`
- Commit each branch separately, then `git push origin <branch>` for all 6.
- Language-branch files are CRLF in the worktree; match the file's line endings when editing with scripts.

## `_shared` submodule

- `docs/source/_shared` = the `sf-shared` repo (content-only shared docs). Each branch must keep its
  submodule gitlink on the matching sf-shared language branch:
  `docs`→`main`, `docs-de`→`docs-de`, `docs-es`→`docs-es`, `docs-fr`→`docs-fr`, `docs-it`→`docs-it`, `docs-ja`→`docs-ja`.
- **Never** commit a gitlink pointing to sf-shared `main` (English) in a language branch — translated
  sites then build with English shared pages (happened 2026-09).
- Before committing in a language branch, verify:
  `git ls-tree HEAD docs/source/_shared` + `git -C docs/source/_shared branch -r --contains <sha>`.
- sf-shared commit messages are English in every branch (histories mirror `main`) — judge branch
  membership with `--contains`, not by the message.
- To move the gitlink without initializing the submodule:
  `git update-index --cacheinfo 160000,<sha>,docs/source/_shared`, then commit.
- Full details: `docs/source/_shared/CLAUDE.md`.

## Page widgets (design decisions, updated 2026-09-21)

- **Top nav bar**: injected by `docs/source/_templates/layout.html` (`{% block extrabody %}`) +
  CDN assets `https://ezblock.cc/readDocFile/custom.js|css`. Nav items are built by `custom.js` —
  it contains **no** language menu.
- **Language switcher = the Read the Docs addons flyout** (`<readthedocs-flyout>`), injected by RTD
  at page runtime. There is exactly ONE flyout per site. Its corner position and enabled state are
  **per-project settings in the RTD dashboard** (Settings → Addons → Flyout Menu), not in the repo.
  Default position is bottom-right; `position: null` in the addons API means the default.
  - **Target state (2026-09-21)**: keep the flyout as the language switcher (move it to bottom-left
    via each project's dashboard if desired). Do **not** hide it with CSS — an earlier attempt was
    reverted because the flyout is the only language-switching UI.
  - Dashboard states as of 2026-09-21: `raphael-kit-ja` has flyout **disabled**; en/de/es/fr/it enabled.
- **AI customer-service widget**: a DocsBot widget was briefly mounted in `_templates/layout.html`
  and removed on 2026-09-22 — the team handles the AI after-sales widget by other means. Do not
  re-add widget scripts to `layout.html` without checking with the team first.
- `_static/lang.js`: browser-language redirect banner (top-right notification, auto-redirects on the
  default page) — not a corner switcher.
- `conf.py` `html_theme_options` must stay empty: `flyout_display` is obsolete since sphinx_rtd_theme
  2.0 (the theme no longer renders a flyout; RTD injects its own). Theme in use: sphinx_rtd_theme 3.x.

## Commit style

- Conventional commits, e.g. `fix(docs): ...`, `feat(docs): ...`, `chore(docs): ...`.
- Docs changes are pushed to all 6 branches (per-topic commits, one per branch).
