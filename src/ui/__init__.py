import os

def get_default_theme_dir():
    import platform
    import re
    # it is actually the hostname, but it should match normally :-)
    if re.match("Nokia-N[0-9]{3}.*", platform.node()):
        return os.path.join(os.path.expanduser("~"), "MyDocs", "Uberqt-themes")
    # default linux path
    return os.path.join(os.path.expanduser("~"), ".config", "uberclock", "uberqt-themes")