# buddy

Claude Code companion reroller & manager.

Search, preview, patch, and customize your Claude Code buddy companion. Turn your common chonk into a legendary shiny dragon.

## How it works

Claude Code's buddy system generates your companion deterministically from `hash(yourUUID + SALT)`. The SALT is a 15-character string hardcoded in the binary. By replacing it with a different string of the same length, you get a completely different companion — while staying logged into your own account.

```
hash("your-uuid" + "friend-2026-401")  →  ★ Common Chonk
hash("your-uuid" + "sWCYWCN8hT-8yXH")  →  ★★★★★ Legendary Shiny Dragon
```

The tool brute-forces millions of candidate SALTs per second using Bun to find one that produces exactly the companion you want.

## Install

```bash
# Clone
git clone git@github.com:Yan-Yu-Lin/buddy-cli.git
cd buddy-cli

# Install to PATH
cp buddy ~/.local/bin/buddy
chmod +x ~/.local/bin/buddy
```

Requires: `bun`, `python3 ≥ 3.11`, `codesign` (macOS)

First run auto-installs Python deps (`click`, `rich`) via uv.

## Usage

```bash
# See your current companion
buddy current

# Search for a specific combo
buddy search "legendary dragon"
buddy search "legendary shiny dragon wizard"
buddy search "legendary shiny dragon wizard bullseye"
buddy search "epic cat crown"
buddy search "shiny ghost"

# Filter by stats
buddy search "legendary dragon" --min-stat DEBUGGING:90
buddy search "legendary capybara" --sort SNARK

# Preview without patching
buddy preview <salt>

# Apply a salt (patches binary + clears companion for re-hatch)
buddy patch <salt>

# Set custom name and personality
buddy name "Gristwick"
buddy personality "A fire-breathing debugger who judges your code silently."

# Show ASCII sprite
buddy sprite

# Export as JSON
buddy export

# Undo everything
buddy restore

# How the system works
buddy info
```

## Workflow

```bash
# 1. Find your dream companion
buddy search "legendary shiny dragon wizard bullseye"

# 2. Pick a salt from results
# ★★★★★ LEGENDARY ✨ dragon ◉ [wizard] | best: DEBUGGING:100 | salt: sWCYWCN8hT-8yXH

# 3. Patch
buddy patch sWCYWCN8hT-8yXH

# 4. Restart Claude Code → /buddy

# 5. (Optional) Custom name
buddy name "Mythos"
```

## Search terms

| Category | Values |
|----------|--------|
| Rarity | `common` `uncommon` `rare` `epic` `legendary` |
| Species | `duck` `goose` `blob` `cat` `dragon` `octopus` `owl` `penguin` `turtle` `snail` `ghost` `axolotl` `capybara` `cactus` `robot` `rabbit` `mushroom` `chonk` |
| Eyes | `dot`(·) `star`(✦) `cross`(×) `bullseye`(◉) `at`(@) `circle`(°) |
| Hats | `crown` `tophat` `propeller` `halo` `wizard` `beanie` `tinyduck` |
| Other | `shiny` (1% chance, stacks with rarity) |

## Rarity odds

| Rarity | Chance | With shiny |
|--------|--------|------------|
| Common | 60% | 0.6% |
| Uncommon | 25% | 0.25% |
| Rare | 10% | 0.1% |
| Epic | 4% | 0.04% |
| Legendary | 1% | 0.01% |

Add specific species (1/18), hat (1/7), and eyes (1/6) for the full combo probability.

Legendary + Shiny + specific species + specific hat + specific eyes ≈ **0.000013%**

## Platform support

| Platform | SALT patch (native) | npm patch | Status |
|----------|-------------------|-----------|--------|
| **macOS (arm64)** | ✅ | ✅ | Tested, fully working |
| **macOS (x86)** | Probably ✅ | ✅ | Untested, same approach should work |
| **Linux** | ⚠️ Needs adjustment | ✅ | SALT exists in ELF binary too, but paths differ and no `codesign` needed |
| **Windows** | ❓ | ✅ | Unknown binary format, npm patch should work |

The native binary patch replaces a string inside the Claude Code binary. On macOS this is a Mach-O arm64 executable that requires ad-hoc re-signing after modification (`codesign --force --sign -`). On Linux the binary is ELF and doesn't need signing — but the install paths (`~/.local/share/claude/versions/`) may differ.

The npm/claudesp patch edits `cli.js` (plain JavaScript) and works on any platform.

## After Claude Code updates

Updates overwrite the binary, resetting the SALT. Just run `buddy patch <salt>` again. Your companion's name and personality survive (stored in `~/.claude.json`), but the visual traits (species, rarity, hat, eyes) recompute from the hash — so they'll revert to your original roll until you re-patch.

## How the algorithm works

```
Bun.hash(userId + SALT) → Mulberry32 PRNG seed → sequential rolls:
  1. Rarity    (weighted: 60/25/10/4/1)
  2. Species   (18 types, equal 1/18)
  3. Eye       (6 styles, equal 1/6)
  4. Hat       (7 types if non-common, else none)
  5. Shiny     (1% independent)
  6. Stats     (1 peak, 1 dump, 3 mid — floor based on rarity)
```

**Important**: The native binary uses `Bun.hash()` and the npm version uses FNV-1a. Same UUID + same SALT = **different companion** depending on runtime. This tool uses Bun for search (matching the native binary).

## Files

- `buddy` — the CLI tool (Python, uv inline script)
- `sprites_data.py` — ported ASCII sprite data from Claude Code source (reference)
