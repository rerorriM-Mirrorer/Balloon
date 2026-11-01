# Balloon (A development fork)

Windower 4 NPC dialogue balloons; based on Hando, Yuki, Kenshi, and Ghosty's Balloon 0.13. Original copyright/license terms remain in `Balloon.lua`.

**Status:** Batch 02 is a fresh-install positioning/theme test on `development/balloon-b02-centered-20261101`. It has NOT been smoke-tested or live-tested in FFXI. `master` remains the preserved upstream baseline.

## Installation / updating
Download the complete Batch 02 branch ZIP from GitHub, extract the repository folder, and copy the addon contents to `Windower4/addons/Balloon/` (including `Balloon.lua`, `defaults.lua`, `ui.lua`, `theme.lua`, and all `themes/` assets). Back up the installed addon folder and its `data/settings.xml` first. For a **genuine fresh-default test**, temporarily move the existing `data/settings.xml` somewhere safe before loading on ONE character. Restore it afterward to recover character-specific overrides. Merely reinstalling the Lua and image files will not reset saved settings.

## Fresh-install defaults (Batch 02)
- Display mode 2 (balloon and chat log), FFXI theme, scale 1.5, portraits **off**.
- Prompt bounce on; text speed 10 characters/frame; promptless timeout 10 seconds; movement closing off.
- Dialogue background **center** at 50% of client width and 80% of client height: `(1920, 1728)` at 3840×2160, `(640, 576)` at 1280×720. The anchor scales with the active client resolution; `//bl reset` returns to it.
- Existing saved character/global settings take precedence and are never forcibly rewritten. The newer November 1 XML has movement closing on globally, Cioara's text speed 2 / delay 6 / `xi` theme, and Clairvaux's position `(1965,1720)`; those are preserved as *saved preferences*, not automatically promoted into these new-install defaults.

## FFXI background
Batch 02 restores the **original upstream FFXI dialogue background** as `themes/ffxi/balloon.png`. An identical copy remains at `balloon-classic.png`. Our Batch 01 top-alpha-100/bottom-alpha-240 custom gradient is preserved under `themes/ffxi/balloon-gradient.png`, but is not selected by default. To test that gradient, back up `balloon.png`, copy `balloon-gradient.png` over `balloon.png`, then reload. The developer-only `tools/build_ffxi_background.py` recreates the custom image and writes to `balloon.png` if used; it is not part of ordinary installation.

The FFXI nameplate, portraits, fonts, dialogue/control-byte parsing, and other themes remain unchanged.

## Commands
```
 //bl                         Show help
 //bl help                    Show help
 //bl restart                 Restart this addon
 //bl unload                  Unload this addon
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
 //bl reset                   Center dialogue at 50% width / 80% height
 //bl test Iroha : Hello!     Display test NPC dialogue
 //bl debug off               Disable verbose legacy diagnostic modes
```
See `docs/FORKS.md` for the comparison with ConsoleBGPlus and newer Balloon forks.

The text-speed implementation remains frame-rate-dependent. Improvements there are reserved for the measured rendering pass.

## Compatibility investigation: SirPopAlot / SlowEnter / NPCMirror
Balloon remains presentation-only. It never injects NPC menu choices or intentionally delays input. SirPopAlot currently has explicit waits including an extra 1.5 seconds after detecting event status; changing that is not part of this patch.

Test at the same NPC with `//bl 0`, then `//bl 2`, then `//bl text_speed 0`. Use `//bl trace on` to record visual presentation transitions. Trace has second-resolution timestamps; it does not prove precise subsecond causality.

## Changelog
- **Batch 02 (2026-11-01, UNTESTED IN GAME):** New-install anchor centered at 50% width / 80% height across client resolutions; upstream classic FFXI background restored as default asset; optional custom gradient retained separately; version bumped for testing; saved settings unaffected.
- **Batch 01 (2026-10-14, UNTESTED IN GAME):** Cioara-based defaults; translucent FFXI field with original backup; per-message cancellable timeout (including decimals); one cooperative movement watcher; keyboard release cleanup; correct timed Scroll Lock reopen; input validation; `status` and `trace`; NPC portrait/background lookup cache; setup/testing documentation.
