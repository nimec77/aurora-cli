# Aurora CLI - Flutter for Aurora OS

### Available

Get available versions flutter.

**Example**

```shell
aurora-cli flutter available
```

### Install

Install Flutter SDK for Aurora OS.

**Params**

* `--latest (-l)` - Aurora select latest version for install.

**Example**

```shell
aurora-cli flutter install --latest
```

### Installed

Get installed list Flutter SDK.

**Example**

```shell
aurora-cli flutter installed
```

### Remove

Remove Flutter SDK.

**Example**

```shell
aurora-cli flutter remove
```

### Build

Add script to project for build Flutter application.

**Params**

* `--index (-i)` - Specify index version.
* `--yes (-y)` - All yes confirm.

**Example**

```shell
aurora-cli flutter build
```

### Debug gdb

Project configure and run for gdb debug.

**Params**

* `--index (-i)` - Specify index device.
* `--verbose (-v)` - Detailed output.

**Example**

```shell
aurora-cli flutter debug gdb
```

### Debug dart

Project configure and run on device for dart debug or hot reload.

**Params**

* `--index (-i)` - Specify index device.
* `--emulator (-e)` - Run on emulator.
* `--yes (-y)` - All yes confirm.
* `--verbose (-v)` - Detailed output.

**Example**

```shell
aurora-cli flutter debug dart
```

### Plugins

Get types plugins info. Run in folder with pubspec.yaml.

**Example**

```shell
aurora-cli flutter plugins
```

### Icons

Create icons size for flutter project.

**Params**

* `--path (-p)` - Path to image.

**Example**

```shell
aurora-cli flutter icons -p {/path/to/file.png}
```
