import pandas

def push_repo(local_path, branch_name, ssh_key_path):
    repo = git.Repo(local_path)

    remove_all_ssh_keys_from_agent()  # Remove all keys from the SSH agent
    add_ssh_key_to_agent(ssh_key_path)  # Add the current key to the SSH agent

    with repo.git.custom_environment(GIT_SSH_COMMAND=f'ssh -i {ssh_key_path}'):
        repo.git.add('--all')
        try:
            repo.git.commit('-m', 'Automated commit message')
        except git.exc.GitCommandError as e:
            print(f"No changes to commit: {e}")

        repo.git.push('origin', branch_name)

    # Wait for a random amount of time between 60 to 300 seconds
    wait_time = random.randint(60, 300)
    print(f"Waiting for {wait_time} seconds before the next operation.")
    time.sleep(wait_time)


if __name__ == '__main__':
    print("yes"）
