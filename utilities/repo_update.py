#!/usr/bin/env python

from subprocess import call

git_fetch_command = "git fetch"
git_stash_save_command = "git stash save -u \"repo_update_temp\""
git_pull_rebase_command = "git pull --rebase"
git_stash_pop_command = "git stash pop"
call(git_fetch_command 
     + " && "
     + git_stash_save_command
     + " && "
     + git_pull_rebase_command
     + " && "
     + git_stash_pop_command,
     shell=True)
