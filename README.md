# Action to read package version from pubspec.yaml

Finds the row containing `version:` and extract the version that comes thereafter.

## Usage

```
name: Example action
on: [push]
jobs:
  example-job:
    name: Example
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: RCSandberg/dart-read-package-semantic-version-action@main
        id: call-action
        with:
          path: assets/with-build.yaml
      - run: echo "Read semantic version ${{ steps.call-action.outputs.package-semantic-version }}"
      - run: echo "Read version ${{ steps.call-action.outputs.package-version }}"
      - run: echo "Read version ${{ steps.call-action.outputs.package-build-version }}"
```

## Output Example

Having the line `version: 1.2.3+4` will produce the output:

| Output  | Value |
| ------------- | ------------- |
| package-semantic-version  | 1.2.3+4  |
| package-version  | 1.2.3  |
| package-build-version  | 4  |


## Input
**`path`** - Sets the path to the pubspec.yaml file relative to workspace directory.\
**Optional**&nbsp;&nbsp; Defaults to `./pubspec.yaml`