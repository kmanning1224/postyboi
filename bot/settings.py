import os
DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    from settings_files import env
else:
    from settings_files import env