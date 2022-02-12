from cmath import exp
from pkg.github.client import get_github_client
from pkg.helper import read_output
from pkg.read_token import get_access_token
from github.GithubException import BadCredentialsException, GithubException

output_file_name = "output"
delete_token_path = ""

lines =  read_output(output_file_name)
total_count = len(lines)

gh = get_github_client(get_access_token(delete_token_path))
me = gh.get_user()

counter = 0
for line in lines:
    counter = counter + 1
    repo_name = line.rstrip("\n")
    print("deleting repo - {0} {1}/{2}".format(repo_name, counter, total_count))

    try:
        repo = me.get_repo(repo_name)
        repo.delete()
    except BadCredentialsException as err:
        print("Unable to conenct to github {0}".format(err))
        exit()
    except GithubException as err:
        print("Error deleting repo {0}".format(err))
    except Exception as err:
        print("unknown error on repo {0}".format(err))

