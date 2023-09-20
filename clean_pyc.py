import os

# Recursively find and delete .pyc files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pyc"):
            full_path = os.path.join(root, file)
            os.remove(full_path)
