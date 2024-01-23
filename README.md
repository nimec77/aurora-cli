# Aurora CLI 2.0

An application that simplifies the life of an application developer for the Aurora OS.
The application is under development.

## Features

* sdk
  - available - Get available version Aurora SDK.
  - install - Download and run install Aurora SDK.
* psdk
  - available - Get available version Aurora Platform SDK.
  - install - Download and run install Aurora Platform SDK.
  - installed - Get installed list Aurora Platform SDK.
  - sudoers - Add sudoers permissions Aurora Platform SDK.
  - remove - Remove installed Aurora Platform SDK.
  - sign - Sign (with re-sign) RPM package.
* device
  - available - Get available devices from configuration.
  - command - Execute the command on the device.

## Usage

```
# Clone project
git clone https://github.com/keygenqt/aurora-cli.git

# Open folder project
cd aurora-cli

# Init environment
virtualenv .venv

# Open environment
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run app
python -m app
```

### License

```
Copyright 2023 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
