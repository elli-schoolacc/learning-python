import menu_decoration, menu_games, menu_preferences, menu_profile, menu_security, menu_admin

menu = {
            '1': ('Security', menu_security.menu_security()),
            '2': ('Decorations', menu_decoration.menu_decoration()),
            '3': ('Games', menu_games.menu_games()),
            '4': ('Admin', menu_admin.menu_admin()),
            'p': ('Preferences', menu_preferences.menu_preferences()),
            'v': ('ViewProfile', menu_profile.menu_profile()),
            'q': ('Quit', print("exit"))
        }

def a():
    return