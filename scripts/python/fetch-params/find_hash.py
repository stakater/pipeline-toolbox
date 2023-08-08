

def find_hash(provider, username, password, hash, workspace, repository):
  if provider == "bitbucket":
    fetch_params_bitbucket(args.provider, args.username, args.password, args.hash, args.workspace, args.repository)
  elif provider == "github":
    fetch_params_github(args.provider, args.username, args.password, args.hash, args.workspace, args.repository)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("provider", help="Name of git provider")
    parser.add_argument("username", help="Username for git provider")
    parser.add_argument("password", help="Password/Token for provider")
    parser.add_argument("hash", help="Hash of the commit that triggered the pipeline")
    parser.add_argument("workspace", help="Workspace/Organization")
    parser.add_argument("repository",  help="Git repository name")
    args = parser.parse_args()
    find_hash(args.provider, args.username, args.password, args.hash, args.workspace, args.repository)
#     fetch_params_bitbucket(args.provider, args.username, args.password, args.hash, args.workspace, args.repository)
