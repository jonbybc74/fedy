# Contributing to Fedy

We welcome all contributions. There are a few ways to get involved:

* [Create issues][gh-fedy-issues] for bugs or feature requests
* Create [pull requests] with your awesome patches
* Donate for infrastructure costs and project development

## Creating issues

Guidelines needed.

## Development

Summary needed.

### Get the source code

```
$ git clone https://github.com/folkswithhats/fedy.git
```

### Dependencies

Dependencies needed.

### Writing plugins

Plugins can be placed under `~/.local/share/fedy/plugins/`, or in the system
plugins directory.

Each plugin is a directory with the suffix `.plugin`, which consist of a JSON
formatted metadata file. The metadata file contains information about the
plugin and describes how `Fedy` should run the tasks.

The plugins can run any command or scripts (`bash`, `python` etc.). In addtion
to the system commands, `Fedy` provides an additional command, `run-as-root` to
allow running commands (e.g.- `run-as-root touch /some/file/somewhere`) or
scripts (e.g.- `run-as-root -s do-stuff.sh`) as root.

Have a look at the existing plugins to know more about how to write plugins for
`Fedy`.

### Special thanks

The following people helped contribute to Fedy in some way, but do not have git
commits. We thank you:

- Alin Andrei
- Dave Smith
- Dave Wilks
- Francisco Villarroel
- Reda Lazri
- TingPing
- Valdur Kana

[gh-fedy-issues]: https://github.com/folkswithhats/fedy/issues
[gh-fedy-pulls]: https://github.com/folkswithhats/fedy/pulls
