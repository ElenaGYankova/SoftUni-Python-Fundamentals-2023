usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        modified_username = username.replace("-", "")
        modified_username = modified_username.replace("_", "")
        if modified_username.isalnum():
            print(username)
