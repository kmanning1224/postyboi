import os
DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    from settings.development import *
else:
    from settings.development import *