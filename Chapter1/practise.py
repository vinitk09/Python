print('''Twinkle Twinkle little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle Twinkle little star,
How I wonder what you are!
      ''')


# External module -> External modules are those that need to be installed separately. They are not included in the standard Python library and must be downloaded and installed from external sources, such as the Python Package Index (PyPI). External modules can provide additional functionality and features that are not available in the built-in modules.
# import pyttsx3

# engine = pyttsx3.init()

# engine.say('''Twinkle Twinkle little star,
# How I wonder what you are!''')
# engine.runAndWait()



import os
directory_path = "/"

contents = os.listdir(directory_path)

for item in contents:
    print(item)


