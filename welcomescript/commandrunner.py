import menu_decoration, menu_games, menu_preferences, menu_profile, menu_security

def CommandRunner():
    menu = {
        '1': ('Security', security_settings),
        '2': ('Decorations', decorations),
        '3': ('Games', games),
        'p': ('Preferences', preferences),
        'v': ('ViewProfile', view_profile),
        'q': ('Quit', quit)
    }
    