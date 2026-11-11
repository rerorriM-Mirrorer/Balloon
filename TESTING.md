# TESTING.md — Balloon B02 countdown-hidden patch (2026-11-11)

**Current patch:** `development/balloon-b02-hide-timer-20261111`, based on the latest B02 centered-theme work. **No live Windower/FFXI test yet.** The original B02 branch and `master` remain untouched.

## Installation and verification

1. Back up `Balloon/ui.lua`. For the minimal patch, replace only this one file with the patched file from the branch, or download the branch ZIP and copy only `ui.lua` into `Windower4/addons/Balloon/`. Keep the existing data/settings and theme assets.
2. Reload with `//lua reload balloon` (or use `//bl restart`).
3. Trigger a normal **promptless/timed** NPC message: the text and background should still appear, but the numeric countdown should be invisible.
4. Confirm the message still disappears after `NoPromptCloseDelay` seconds (the saved setting is preserved). With `//bl delay 1.5`, it should close after about 1.5 seconds, with no visible countdown.
5. Trigger prompted NPC dialogue: the ordinary advance arrow still appears. Scroll Lock hide/reopen should not resurrect the timer.
6. Check a repeated NPC interaction or quick next line: the previous message's timeout must not prematurely close the new message.

### Change and verification

- **Code:** `ui.lua` changes only the timed-dialogue UI visibility, `self.timer_text:show()` to `self.timer_text:hide()`. `Balloon.lua` is **not modified**; the same countdown timer, timeout cancellation, dialogue close, and `//bl delay` behavior remain.
- **Static review:** the sole display call was identified in `ui:show(timed)`. The timer updates and expiration remain in `Balloon.lua`. A static grep/source comparison does not prove in-game behavior.
- **Known limitations:** the timer text object may still be created and updated internally as before; nothing renders it. No new configuration toggle or new visuals.
- **Delivery:** patch commit `bbde48f24ce46298a92133d68004448eedecab2e`, plus documentation updates on the same branch.

## Earlier cumulative testing record (preserved below)

---

# TESTING.md — Balloon Batch 02 (2026-11-01)

**Current test:** Fresh-install placement and classic FFXI theme, on `development/balloon-b02-centered-20261101`. This change has NOT been tested in a running Windower/FFXI client. `master` is unchanged.

## B02 installation and verification

1. Back up your existing `Windower4/addons/Balloon/` and especially `Balloon/data/settings.xml`.
2. Download the full B02 branch ZIP from GitHub, extract its repository folder, and install all its contents under `Windower4/addons/Balloon/` (not nested under a second `Balloon` folder). Keep `themes/`, the Lua files, `README.md`, `WORKFLOW.md` and this `TESTING.md` together.
3. For a genuine **fresh settings** test on ONE character, temporarily move `data/settings.xml` outside the addon. Leave it backed up: do not permanently delete your settings. A fresh source install with an old settings file will intentionally keep old character/global coordinates and theme.
4. Load with `//lua load balloon` (or log in), check `//bl status`, and run `//bl test TestNPC : Hello from Balloon`.
5. On 3840×2160, expect the **center of the dialogue background** to be (1920,1728), exactly 50% across and 80% down. It is not the top-left corner. Confirm the original upstream FFXI backdrop is in use (not the Batch 01 custom gradient).
6. Drag the balloon, then use `//bl reset`. Confirm it returns to (1920,1728), is still fully visible, and keeps the layout and text legible.
7. Repeat at a smaller active game/UI resolution if available: 1280×720 should anchor at (640,576); 960×540 should anchor at (480,432). Observe clipping and alignment, especially with scale 1.5.
8. Restore the backed-up settings after fresh-default testing and reload. Confirm custom position / text speed / theme / delay still take precedence. On the user's November 1 example, Cioara has custom `xi` theme and Clairvaux has (1965,1720); `xi` is a locally renamed theme not included in this repository, so restore that local theme directory if needed.
9. Recheck promptless timeout, prompts, movement and Enter behavior from the B01 tests below; report any changes or Lua errors.

### B02 acceptance checklist

- [ ] Fresh config selects theme `ffxi` and original image, with mode 2, scale 1.5, portraits off, animated prompt on, text speed 10, promptless delay 10, movement closes off.
- [ ] Fresh config at 3840×2160 centers backdrop at (1920,1728).
- [ ] `//bl reset` returns to same resolution-scaled anchor after a drag.
- [ ] 1280×720 / 960×540 default anchors as above, with acceptable on-screen visibility.
- [ ] Existing custom per-character/global XML survives an upgrade; local `xi` theme must exist if referenced by saved settings.
- [ ] `//bl status` shows version `0.13-a.20261101.2` and current settings; no loading errors.
- [ ] Basic prompted/timed dialogue, Enter, Scroll Lock, movement watcher, and reload remain functional.

### B02 scope, verification and source

- **Implemented:** `defaults.lua` uses 50%/80% of Windower `ui_x_res`/`ui_y_res`; original upstream FFXI PNG is the normal `balloon.png` (Git blob `64f1082a...` matches StarlitGhost/Balloon); previous gradient retained as `balloon-gradient.png`; version string updated.
- **Intentionally unchanged:** Text speed, delay, movement-closing behavior and all saved XML; no timer or input redesign. The November 1 user XML is a preference reference, not a replacement preset.
- **Static/source verification:** The source tree and original-art blob were inspected using GitHub; simple position arithmetic gives the anchors above. No Lua 5.1/Windower runtime is available in this execution environment; game behavior is **not verified**.
- **Code commits:** `fa027a8` (placement and artwork), `600cb99` (version). Documentation commits follow on the same branch; see current branch history.
- **Feedback to record:** screenshot or description of position, tested client resolution, whether existing `settings.xml` was moved, exact theme, `//bl status`, and any reported errors.

## B01 historical testing instructions (preserved)

The following was recorded for Batch 01 on October 14–16, before Batch 02 restored the original background. Descriptions of the custom background as the active `ffxi/balloon.png` are **historical B01 expectations**, not B02 defaults.

---

# TESTING.md — Balloon Batch 01

**Read this before installing.** This branch contains unverified Windower-side changes. It has NOT been smoke-tested or live-tested in FFXI. The original `master` and `themes/ffxi/balloon-classic.png` remain preserved.

## Install
1. Back up your current installed Balloon folder and its `data/settings.xml`.
2. Download the development branch's source as a ZIP or copy its full folder to `Windower4/addons/Balloon/`. Keep `themes/`, `ui.lua`, `defaults.lua`, `theme.lua`, and `Balloon.lua` together.
3. Reload on **one** test character first, not all six clients. If you are unable to load, restore the original folder and report the exact Lua error.
4. Use `//bl help`, `//bl status`, then `//bl test TestNPC : Hello from Balloon`.

## Priority live test sequence (record actual observed results)
- [ ] Loads at log-in and with `//lua load balloon`, without Lua errors. `//bl restart` and `//bl unload` work once and without leftover UI.
- [ ] On a character with no saved configuration: defaults are FFXI theme, scale 1.5, portraits off, DisplayMode 2. Existing Cioara/Myrr overrides still win.
- [ ] New FFXI texture uses alpha 100 top/240 bottom, comparable to ConsoleBGPlus's 100/250 setting; compare with `balloon-classic.png`. Check readability on bright scenes.
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
- Source commits include: `5b8f64a` Cioara defaults; `330b1f5` timers/keyboard/trace; `20038f4` initial FFXI texture; `1347168` lookup cache; `021c444` reproducible gradient builder; `780a6c2` calibrated gradient; `b800492` restart/unload; `6ed3965` fork comparison. Use the branch log for the complete sequence.
- Source of preferences: Cioara settings XML (global display 2, movement off, timeout 10, text speed 10; Cioara position 1922/1796, scale 1.5, theme ffxi, portraits off).
- Report errors with client, resolution, exact NPC/action, whether SlowEnter/SirPopAlot were loaded, and `//bl status` result.

## Historical results
None yet. Do not mark tests passed without observing them. Record later corrections without erasing the original findings.

## Agent instructions adoption — 2026-10-16

- Added `AGENTS.md` at this development branch's repository root to direct coding agents to the current workflow and testing records, with a canonical NPCMirror fallback when documents are missing.
- Documentation commit: [`654def47`](https://github.com/rerorriM-Mirrorer/Balloon/commit/654def47c42b54a3070436c8a2a2516e2f4fc668).
- No addon code was changed or game testing performed as part of this documentation update; all previous test instructions and observations remain above.
