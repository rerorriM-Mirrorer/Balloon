# Balloon fork and UI reference survey (2026-10-14)

These are **candidate** features, not cherry-picked code. Current Batch 01 is built on the unchanged StarlitGhost 0.13 source in rerorriM-Mirrorer/Balloon.

## Alden Park / Balloon 0.16
Source: https://github.com/aldenpark/Balloon

- `SystemMessages` toggles whether mode-151 dialogue enters Balloon.
- `AdditionalChatModes` lets the user opt into specific additional modes. Its default excludes mode 142 because fishing/item notices may be caught accidentally.
- A special Grounds Tome/Field Manual multi-line flow in mode 1 preserves the final "Training area" prompt instead of hiding the choice. This mutates text/advance behavior and needs careful testing against SlowEnter/NPCMirror before being adopted.
- `//bl debug input` writes a dedicated input/dialogue trace, but this can record dialogue content and should be explicit opt-in.
- New alternative FFXI Window 5 and solid Window 5 themes (plus xiPrime-style art). Consider as separately selectable themes; don't replace the saved default until reviewed.
- Improved speaker/background order: set message type and then let a special NPC graphic replace just the backdrop. Worth backporting after scene regression tests.
- README mentions a dark-fade theme, but the examined current theme directory did not contain a `dark-fade` folder; verify before claiming it is available.

## KenshiDRK / Balloon
Source: https://github.com/KenshiDRK/Balloon

- Optional `//bl translate` and `//bl language` support, backed by `Translator` and `Languages` modules. Language/argument validation requires review; external translation may stall or change story text.
- Best explored separately, opt-in, and with a bounded asynchronous translation pipeline so core dialogue remains instant.

## Ashita v4 port
Source: https://github.com/onimitch/ffxi-balloon-ashitav4

- Useful reference for text and image handling across clients, but Ashita event/image APIs are not drop-in compatible with Windower 4.

## ConsoleBGPlus comparison
Source: https://github.com/rerorriM-Mirrorer/Windower-Addons/tree/consolebg-plus

- `addons/ConsoleBGPlus/cbg_layout.lua` and `tools/consolebgplus/build_skin.py` preserve native XIVParty-derived thin violet stripes, separately drawn silver rails, a gentle bottom glow, and live-adjustable top/bottom opacity. Current documented defaults are top 100, bottom 250, alpha 255.
- Balloon's first FFXI background uses top 100 and bottom 240 alpha with dark-navy rows and lighter thin stripes. This is a single texture (cheap to render) and is **not** yet a live-adjustable multi-part panel.
- The original Balloon FFXI art is preserved as `themes/ffxi/balloon-classic.png`. `tools/build_ffxi_background.py` can regenerate the experimental texture. The texture should be compared in-game with bright and dark scenes.
- If more nuanced fades or edit-time gradient controls are wanted, reuse the ConsoleBGPlus independent fill/rail layering concept rather than blindly merging full layouts or recreating its asset bundle.

## Recommended next steps (no changes in this batch)
1. Confirm new gradient readability and fix any PNG or font alignment errors.
2. Measure dialogue arrival, open, displayed, Enter, and close timestamps on the same SirPopAlot NPC; instrument SirPopAlot separately to distinguish its 1.5s wait from Balloon work.
3. Adopt optional system-message filtering and other modes; keep story progression safe by default.
4. Adopt additional themes as options, not as defaults.
5. Consider reversible whole-UI layout/edit/fade controls and frame-independent text reveal.

Everything above is a source review; no claim of in-game verification.
