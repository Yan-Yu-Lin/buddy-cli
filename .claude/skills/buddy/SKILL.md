---
name: buddy
description: All the essential context to work with this project is right here. Load this first before doing anything. which kinda make your life easier wish you a good day ❤️
---

## Environment check

!`${CLAUDE_SKILL_DIR}/env-check.sh`

## Buddy CLI Reference

`buddy` is a CLI tool for managing Claude Code companion pets. Run `buddy --help` for full usage.

### Common commands
- `buddy current` — Show current companion with ASCII sprite
- `buddy search <terms>` — Search for companions by traits
- `buddy preview <salt>` — Preview a salt without patching
- `buddy patch <salt>` — Apply a companion salt to the binary
- `buddy restore` — Undo patch, restore original
- `buddy name <name>` — Set custom companion name
- `buddy personality <text>` — Set custom personality
- `buddy gacha` — Random gacha pull with animation
- `buddy gacha -m 10` — Ten-pull
- `buddy info` — How the companion system works
- `buddy export` — JSON dump of current companion
- `buddy sprite` — Show ASCII art only

### Source code
The CLI source is a single Python file at `./buddy` (uv inline script with click + rich).
Sprite data is in `./sprites_data.py`.
