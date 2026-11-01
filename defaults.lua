local defaults = {}

defaults.DisplayMode = 2
defaults.MovementCloses = false
defaults.NoPromptCloseDelay = 10
defaults.AnimatePrompt = true
defaults.TextSpeed = 10
-- Use the bundled original FFXI theme and background art on new installs.
-- Existing saved settings, including per-character overrides, still win.
defaults.Theme = 'ffxi'
defaults.Scale = 1.5
defaults.ShowPortraits = false

local windower_settings = windower.get_windower_settings()
defaults.Position = {}
-- The dialogue background is centered at this anchor by ui:position.
-- 50% across and 80% down the active client resolution (1920, 1728 at 3840x2160).
defaults.Position.X = math.floor(windower_settings.ui_x_res * 0.5 + 0.5)
defaults.Position.Y = math.floor(windower_settings.ui_y_res * 0.8 + 0.5)

return defaults
