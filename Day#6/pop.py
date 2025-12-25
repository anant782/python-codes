settings = {"theme": "dark", "lang": "en"}

# Pop a key that exists
theme_value = settings.pop("theme")
print(f"Removed value: {theme_value}")  # Output: Removed value: dark
print(f"Dictionary: {settings}")  # Output: Dictionary: {'lang': 'en'}

# Pop a key that does not exist, with a default fallbackprettier.forceFormatDocument
timezone_value = settings.pop("timezone", "UTC")
print(f"Returned value: {timezone_value}")  # Output: Returned value: UTC
print(f"Dictionary: {settings}")  # Output: Dictionary: {'lang': 'en'}
