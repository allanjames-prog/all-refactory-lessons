# files = [
#     "classes-&-objects.md",
#     "conditionals.md",
#     "datatypes 3.md",
#     "dynamic-static.md",
#     "lists.md",
#     "loops.md",
#     "operator-2.md",
#     "operators.md",
#     "sets-and-dicts.md",
#     "string-methods.md",
#     "tuples.md"
# ]

# for filename in files:
#     open(filename, 'w').close()


# import os

# # List of files in the original order
# files = [
#     "classes-&-objects.md",
#     "conditionals.md",
#     "datatypes 3.md",
#     "dynamic-static.md",
#     "lists.md",
#     "loops.md",
#     "operator-2.md",
#     "operators.md",
#     "sets-and-dicts.md",
#     "string-methods.md",
#     "tuples.md"
# ]

# # Define the new filenames (with numbers and hyphen)
# new_filenames = [
#     "01-datatypes.md",
#     "02-operators.md",
#     "03-conditionals.md",
#     "04-dynamic-static.md",
#     "05-lists.md",
#     "06-loops.md",
#     "07-operator-2.md",
#     "08-operators.md",
#     "09-sets-and-dicts.md",
#     "10-string-methods.md",
#     "11-tuples.md"
# ]

# # Loop through the files and rename them
# for old_name, new_name in zip(files, new_filenames):
#     # Ensure the file exists before renaming
#     if os.path.exists(old_name):
#         os.rename(old_name, new_name)
#         print(f"Renamed '{old_name}' to '{new_name}'")
#     else:
#         print(f"File '{old_name}' does not exist.")


# import os

# # List of files in the original order
# files = [
#     "classes-&-objects.md",
#     "conditionals.md",
#     "datatypes 3.md",
#     "dynamic-static.md",
#     "lists.md",
#     "loops.md",
#     "operator-2.md",
#     "operators.md",
#     "sets-and-dicts.md",
#     "string-methods.md",
#     "tuples.md"
# ]

# # Define the new filenames (with numbers and hyphen)
# new_filenames = [
#     "01-datatypes.md",
#     "02-operators.md",
#     "03-conditionals.md",
#     "04-dynamic-static.md",
#     "05-lists.md",
#     "06-loops.md",
#     "07-operator-2.md",
#     "08-operators.md",
#     "09-sets-and-dicts.md",
#     "10-string-methods.md",
#     "11-tuples.md"
# ]

# # Reverse the renaming process (from new filenames back to original filenames)
# for new_name, old_name in zip(new_filenames, files):
#     # Ensure the new file exists before renaming
#     if os.path.exists(new_name):
#         os.rename(new_name, old_name)
#         print(f"Renamed '{new_name}' back to '{old_name}'")
#     else:
#         print(f"File '{new_name}' does not exist.")



import os

# List of files in the original order
files = [
    "classes-&-objects.md",
    "conditionals.md",
    "datatypes 3.md",
    "dynamic-static.md",
    "lists.md",
    "loops.md",
    "operator-2.md",
    "operators.md",
    "sets-and-dicts.md",
    "string-methods.md",
    "tuples.md"
]

# Define the new filenames in the custom order (not just top to bottom)
new_filenames = [
    "01-datatypes.md",       # this would be for "datatypes 3.md"
    "02-operators.md",       # this would be for "operators.md"
    "03-conditionals.md",    # this would be for "conditionals.md"
    "04-dynamic-static.md",  # this would be for "dynamic-static.md"
    "05-lists.md",           # this would be for "lists.md"
    "06-loops.md",           # this would be for "loops.md"
    "07-operator-2.md",      # this would be for "operator-2.md"
    "08-classes-and-objects.md",  # this would be for "classes-&-objects.md"
    "09-sets-and-dicts.md",  # this would be for "sets-and-dicts.md"
    "10-string-methods.md",  # this would be for "string-methods.md"
    "11-tuples.md"           # this would be for "tuples.md"
]

# Loop through the original files and new filenames to rename them
for old_name, new_name in zip(files, new_filenames):
    # Ensure the file exists before renaming
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'")
    else:
        print(f"File '{old_name}' does not exist.")
