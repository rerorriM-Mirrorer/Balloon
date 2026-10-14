# TESTING.md — Balloon Batch 01

**Read this before installing.** This branch contains unverified Windower-side changes. It has NOT been smoke-tested or live-tested in FFXI. The original `master` and `themes/ffxi/balloon-classic.png` remain preserved.

## Install
1. Back up your current installed Balloon folder and its `data/settings.xml`.
2. Download the development branch's source as a ZIP or copy its full folder to `Windower4/addons/Balloon/`. Keep `themes/`, `ui.lua`, `defaults.lua`, `theme.lua`, and `Balloon.lua` together.
3. Reload on **one** test character first, not all six clients. If you are unable to load, restore the original folder and report the exact Lua error.
4. Use `//bl help`, `//bl status`, then `//bl test TestNPC : Hello from Balloon`.

## Priority live test sequence (record actual observed results)
- [ ] Loads at log-in and with `//lua load balloon`, without Lua errors.
- [ ] On a character with no saved configuration: defaults are FFXI theme, scale 1.5, portraits off, DisplayMode 2. Existing Cioara/Myrr overrides still win.
- [ ] New FFXI texture fades at top; compare with `balloon-classic.png`. Check font readability against bright in-game backgrounds.
- [ ] `//bl delay 1.5` closes promptless text rather than sticking; old timer cannot close a newer line.
- [ ] `//bl delay 0` closes immediately; invalid scale, delay, or speed is rejected.
- [ ] With `//bl move_closes`, movement closes only when balloon is active; toggling twice doesn't spawn competing watchers.
- [ ] Enter closes presented balloon; using chat/SlowEnter/other key-blocking addons doesn't wedge future Enter handling.
- [ ] Scroll Lock hides and reopens prompted AND timed balloons appropriately.
- [ ] NPC-specific background returns to ordinary styling when next speaker lacks a special background.
- [ ] Repeated NPC dialogue with portraits off works without portrait assets; toggling portraits on and switching themes still works.
- [ ] SirPopAlot comparison: `//bl 0`, `//bl 2`, `//bl text_speed 0` at the same NPC; test `//bl trace on`. Identify whether timing is game action or display only.
- [ ] Smaller client at 1280×720 or 960×540: no offscreen soft-lock, meaningful field placement.
- [ ] Four-/six-client load: UI updates and frame pacing satisfactory.

## Known risks / deliberately deferred
- The new FFXI texture is a generated approximation, not a pixel edit of upstream art. The original is still available as `balloon-classic.png`. Compare visually before adopting.
- `text_speed` still uses per-frame reveal; decoding has unmodified FFXI control bytes.
- Older per-character XML values persist intentionally; changing Lua defaults does not overwrite them.
- Second-resolution trace is for order of operations, not performance benchmarking.
- Cross-addon action readiness, additional text modes, training-book special behavior, full status/help formatting, automatic layout recovery, and fade animation remain for later batches.
- No runtime Lua syntax checker or Windower instance was available in this pass; inspect errors before treating as live-proven.

## Delivery register
- B01 branch: `development/balloon-b01-cioara-20261014`
- Commits: `5b8f64a` Cioara defaults; `330b1f5` timers/keyboard/trace; `20038f4` FFXI texture with original preserved; `1347168` portrait/background cache.
- Source of preferences: Cioara settings XML (global display 2, movement off, timeout 10, text speed 10; Cioara position 1922/1796, scale 1.5, theme ffxi, portraits off).
- Report errors with client, resolution, exact NPC/action, whether SlowEnter/SirPopAlot were loaded, and `//bl status` result.

## Historical results
None yet. Do not mark tests passed without observing them. Record later corrections without erasing the original findings.
