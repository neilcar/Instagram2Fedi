import hashlib

def already_posted(id, path):
    with open(path) as file:
        content = file.read().split("\n")
        sha1 = hashlib.sha1(bytes(id, "utf-8")).hexdigest()
        if sha1 in content:
            return True
        return False

def mark_as_posted(id, path):
    with open(path, 'a') as file:
        sha1 = hashlib.sha1(bytes(id, "utf-8")).hexdigest()
        file.write(sha1+'\n')

def already_posted_stateless(mastodon, tag, fetched_user):
    statuses=mastodon.search(tag) #, result_type="statuses", account_id=fetched_user)
    if len(statuses.hashtags) >0:
        return True
    return False


