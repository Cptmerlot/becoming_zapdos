import imp
from typing import List
import random
import time

from pkg.github.client import get_github_client

from pkg.helper import random_name, write_output
from pkg.read_token import get_access_token

random.seed(time.time())

amount_of_repos = 75
output_file_name = "output"

gh = get_github_client(get_access_token())
me = gh.get_user()

repo_list: List[str] = []
for i in range(0, amount_of_repos):
    repo_name = random_name("_")
    repo_description = random_name(" ", 4, 8) + "."
    repo_list.append(repo_name)
    print("description {0}".format(repo_description))
    print("creating repo {0} {1} out of {2}".format(repo_name, i, amount_of_repos))

    me.create_repo(repo_name, repo_description)
    sleep_time = random.randint(3, 20)
    print("sleeping for {0} secs".format(sleep_time))
    time.sleep(sleep_time)

write_output(repo_list, output_file_name)