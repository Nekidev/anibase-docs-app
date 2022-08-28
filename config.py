import toml

config = toml.load('.streamlit/config.toml')

THEME_PRIMARY_COLOR = config['theme']['primaryColor']
THEME_BACKGROUND_COLOR = config['theme']['backgroundColor']
THEME_SECONDARY_BACKGROUND_COLOR = config['theme']['secondaryBackgroundColor']
THEME_TEXT_COLOR = config['theme']['textColor']
THEME_FONT = config['theme']['font']
THEME_BASE = config['theme']['base']