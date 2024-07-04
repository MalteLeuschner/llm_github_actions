from github import Github
import os
import sys


def get_changed_files(repo, commit_sha):
    commit = repo.get_commit(commit_sha)
    files = commit.files
    changed_files = [file.filename for file in files if file.filename.
        endswith('.py') and file.filename.startswith('src/test_pythons')]
    return changed_files


def main():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print('GITHUB_TOKEN environment variable is not set.')
        sys.exit(1)
    g = Github(token)
    repo_name = os.getenv('GITHUB_REPOSITORY')
    commit_sha = os.getenv('GITHUB_SHA')
    if not repo_name or not commit_sha:
        print(
            'Required environment variables (GITHUB_REPOSITORY, GITHUB_SHA) are missing.'
            )
        sys.exit(1)
    repo = g.get_repo(repo_name)
    changed_files = get_changed_files(repo, commit_sha)
    for file in changed_files:
        print(file)
    print(f"::set-output name=changed_files::{' '.join(changed_files)}")


if __name__ == '__main__':
    main()
