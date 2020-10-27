Dobhar-chú: the King Otter
==========================

The Dobhar-chú (Irish pronunciation: [ˈd̪ˠaɾˠxuː], lit. "water dog" or "water hound")
or King Otter is a creature of Irish folklore. It resembles both a dog and an otter,
though it sometimes is described as half dog, half fish. It lives in water and has
fur with protective properties.

https://en.wikipedia.org/wiki/Dobhar-ch%C3%BA

`dobharchu` is also an administrative CLI tool to manage various aspects of the Lutris
backend. This project is not intended to be used by regular users. You will require
admin access to the lutris website in order to access the features of this tool.

`dobharchu` will eventually supersede the bash scripts used in the buildbot repo.

Current features
----------------

Add a folder to a runtime: `add-runtime-folder`. This command takes a directory as
the input as well as a --url-prefix and a --runtime parameter. Ex::

    dobharchu add-runtime-folder ~/lutris/icons \
        --url-prefix=https://raw.githubusercontent.com/lutris/lutris-runtime/master/icons/ \
        --runtime icons

This will recursively scan a folder and add every file as a component,
prefixed by `url-prefix` and add them as runtime component. The files must already be present
on the remote location and should be an up to date representation of the folder you are scanning.

In the above example, icons are stored in a git repository. This makes it easy to sync files locally.

