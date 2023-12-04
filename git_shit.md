# Github Credentials

# 2023 

- install gcm with apt-get
- git config --global credential.helper store

---


I was using a password to access via the CLI in Linux.  The 13/8/21 they
discontinued this API. Migration was painful.  Maybe it's because Microsoft wants us to use GUI clients.

Before I started I upgraded the git CLI to the latest version.

### SSH keys

I generated SSH keys locally and installed it on my machine.

- start the ```ssh``` service
- type something like

```ssh-keygen -t ed25519 -C "your_email@example.com"```

- you don't need the email it's just a comment for the file which is 
- stored in ~/.ssh

Copy paste to the window on my account failed repeatedly but I think this was because of vi splitting a line or something.
[help page](https://github.community/t/key-is-invalid-you-must-supply-a-key-in-openssh-public-key-format/170135/4)

**This didn't solve the write access problem**
Actually it may be that using the GPG token forces access via HTTPS and not SSH.  Go figure

### GPG access token

This is very poorly documented
[here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).

- generated the key on my GitHub account and gave it permissions.
- installed GCM from a .deb, had to restart linux because of a lock that blocked dpkg
- ran GCM to configure
- tried pushing my webpage, got asked to go to the browser to authorize, used password and clicked on the form button

They should really have set default permissions on the checkboxes -- I had to delete a couple of keys because I wasn't sure I had set the right ones.

### Try it on another machine


