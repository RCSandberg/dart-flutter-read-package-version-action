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

      # With path set implicitly to default value
      - uses: RCSandberg/dart-read-package-semantic-version-action@v1.0.0
        id: call-action-1
      - run: echo "Read semantic version ${{ steps.call-action-1.outputs.package-semantic-version }}"
      - run: echo "Read version ${{ steps.call-action-1.outputs.package-version }}"
      - run: echo "Read build version ${{ steps.call-action-1.outputs.package-build-version }}"


      # With path set explicitly
      - uses: RCSandberg/dart-read-package-semantic-version-action@v1.0.0
        id: call-action-2
        with:
          path: path/to/pubspec.yaml
      - run: echo "Read semantic version ${{ steps.call-action-2.outputs.package-semantic-version }}"
      - run: echo "Read version ${{ steps.call-action-2.outputs.package-version }}"
      - run: echo "Read build version ${{ steps.call-action-2.outputs.package-build-version }}"
```

## Output Example

Having the line `version: 1.2.3+4` will produce the output:

| Output  | Value |
| ------------- | ------------- |
| package-semantic-version  | 1.2.3+4  |
| package-version  | 1.2.3  |
| package-major  | 1  |
| package-minor  | 2  |
| package-patch  | 3  |
| package-prerelease  | |
| package-buildmetadata  | 4  |


Having the line `version: 1.2.3-alpha-beta-321+build.42` will produce the output:

| Output  | Value |
| ------------- | ------------- |
| package-semantic-version  | 1.2.3-alpha-beta-321+build.42  |
| package-version  | 1.2.3  |
| package-major  | 1  |
| package-minor  | 2  |
| package-patch  | 3  |
| package-prerelease  | alpha-beta-321  |
| package-build-version  | build.42  |


## Input
**`path`** - Sets the path to the pubspec.yaml file relative to workspace directory.\
**Optional**&nbsp;&nbsp; Defaults to `./pubspec.yaml`