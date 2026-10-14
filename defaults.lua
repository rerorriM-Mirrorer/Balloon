local defaults = {}

defaults.DisplayMode = 2
defaults.MovementCloses = false
defaults.NoPromptCloseDelay = 10
defaults.AnimatePrompt = true
defaults.TextSpeed = 10
-- New installs use Cioara's FFXI theme; existing saved settings are never overwritten.
defaults.Theme = 'ffxi'
defaults.Scale = 1.5
defaults.ShowPortraits = false

local windower_settings = windower.get_windower_settings()
defaults.Position = {}
-- Reference: Cioara at 3840x2160 (1922, 1796). Adapt to smaller client windows.
defaults.Position.X = math.floor(windower_settings.ui_x_res * (1922 / 3840) + 0.5)
defaults.Position.Y = math.floor(windower_settings.ui_y_res * (1796 / 2160) + 0.5)

return defaults