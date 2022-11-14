>/ [VST Home](../) / [Tutorials](Index.md)
>
># Switching to another VSTGUI submodule or branch

**On this page:**

[[_TOC_]]

---

Sometimes it is necessary to switch to another ```VSTGUI``` submodule or branch for testing purpose. This tutorial explains how to do that.

---

## Switching to another submodule

Navigate to your local ```VST 3 SDK``` checkout and execute the following command on the command line to switch the submodule.

```shell
git submodule set-url vstgui4 /path/to/vstgui/
git submodule sync
git submodule update --init --recursive --remote vstgui4
```

The path ```/path/to/vstgui/``` should point to a valid VSTGUI repository. Be aware that the ```set-url```command changes the ```.gitmodules``` file.

> Also use ```/``` as delimiter on Windows for local paths e.g. C:/path/to/vstgui/

---

## Switching to another branch

Switch to any other branch by navigating into ```VSTGUI``` submodule and execute ```git checkout```.

```shell
git checkout my_branch
```