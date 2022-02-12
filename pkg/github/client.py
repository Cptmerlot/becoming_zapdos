from github import Github


def get_github_client(token: str) -> Github:
    return Github(login_or_token=token)
