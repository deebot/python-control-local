## Mirror awaiting setup

Destination: https://github.com/deebot/python-controls-local

1. Ensure the GitHub repository is empty and Private if your source is private.
2. Open https://github.com/deebot/python-controls-local/settings/keys and add the following public deploy key with **Allow write access**.

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOfm+pAGUuY2LFlHjgPelWUKBNH9bVHjxdd/gGuLI6jo
```

3. From the engineering-infra workstation checkout run:

```bash
make project-mirror-activate PROJECT=python-controls-local
```

The command requires your own GitHub SSH read access. It verifies an empty destination (or an exact match after a previous activation), performs the first sync, compares Git refs, then enables push-triggered and hourly mirroring. Never add independent GitHub commits.

Automatic transfers are disabled until activation succeeds. This file records the initial setup request, not live mirror status. See Forgejo Settings → Repository → Mirror settings for current status.
