create_read_token_path = ""

def get_access_token(token_path: str = create_read_token_path) -> str:
    with open(token_path) as f:
        token = f.read()
        return token