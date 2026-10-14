# Balloon (A development fork)

Windower 4 NPC dialogue balloons; based on Hando, Yuki, Kenshi, and Ghosty's Balloon 0.13. Original copyright/license terms remain in `Balloon.lua`.

**Status:** Batch 01 is on a development branch and has not yet been live-tested in FFXI. `master` remains the known-good upstream baseline.

## Installation / updating
Copy the **entire** `Balloon` addon folder to `Windower4/addons/Balloon/`, retaining the themes and `ui.lua`/`theme.lua`. Back up your installed folder first. Do not delete `addons/Balloon/data/settings.xml` (where present): the new hardcoded defaults apply to missing/new settings without replacing per-character values.

## Cioara-derived new-install defaults
- Display mode 2 (balloon and chat log), FFXI theme, scale 1.5, portraits **off**.
- Prompt bounce on; text speed 10 characters/frame; promptless timeout 10 seconds; movement closing off.
- Position based on Cioara's saved (1922, 1796) at 3840×2160; proportionally adapted to other client resolutions.
- Existing saved character/global settings take precedence. The supplied XML had a separate global default theme and other characters' preferences; none are forcibly rewritten.

## FFXI background
The `ffxi/balloon.png` dialogue-field texture has a more transparent top and a deeper-blue bottom. The original PNG is preserved as `themes/ffxi/balloon-classic.png`. To revert **only** the visual change, replace `balloon.png` with a copy of `balloon-classic.png` while Windower is closed, then reload.

The FFXI nameplate, portraits, fonts, dialogue/control-byte parsing, and other themes remain unchanged.

## Commands
```
 //bl                         Show help
 //bl help                    Show help
 //bl status                  Current theme, scale, portrait, active state, last close reason
 //bl trace on                Enable compact open/close trace to FFXI chat
 //bl trace off               Disable trace
 //bl 0                       Hide new balloons; leave game log
 //bl 1                       Balloon; suppress most normal log text
 //bl 2                       Balloon and normal log (recommended for cross-addon testing)
 //bl theme ffxi              Select FFXI theme
 //bl scale 1.5               Set scale (0.25 through 4)
 //bl portrait                Toggle portraits
 //bl delay 1.5               Set a decimal promptless timeout (0 through 300 seconds)
 //bl text_speed 10           Characters per frame (0 through 200; 0 = instant)
 //bl move_closes             Toggle close on player movement
 //bl animate                 Toggle prompt animation
 //bl reset                   Reset to Cioara-derived default position
 //bl test Iroha : Hello!     Display test NPC dialogue
 //bl debug off               Disable verbose legacy diagnostic modes
```
The text-speed implementation is still frame-rate-dependent in this first batch. Improvements there are reserved for the measured rendering pass.

## Compatibility investigation: SirPopAlot / SlowEnter / NPCMirror
Balloon remains presentation-only. It never injects NPC menu choices or intentionally delays input. SirPopAlot currently has explicit waits including an extra 1.5 seconds after detecting event status; changing that is not part of this patch.

Test at the same NPC with `//bl 0`, then `//bl 2`, then `//bl text_speed 0`. Use `//bl trace on` to record visual presentation transitions. Trace has second-resolution timestamps; it does not prove precise subsecond causality.

## Changelog
- **Batch 01 (2026-10-14, UNTESTED IN GAME):** Cioara-based defaults; translucent FFXI field with original backup; per-message cancellable timeout (including decimals); one cooperative movement watcher; keyboard release cleanup; correct timed Scroll Lock reopen; input validation; `status` and `trace`; NPC portrait/background lookup cache; setup/testing documentation.
