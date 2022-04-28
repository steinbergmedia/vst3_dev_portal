>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Moduleinfo

An optional moduleinfo.json file can be part of the module file package.

The file contains the same information as the [Module Factory](Index.md#module-factory), plus an optional list of compatible classes.
The file is encoded in a [json5](http://json5.org) format.

This way the host does not need to load the component to know which classes the module provides.

The optional list of compatible classes is used to declare a class to be treated as a one to one replacement for other classes.

An example moduleinfo.json looks like this:

```json
{
  "Name": "helloworld",
  "Version": "3.7.4.0",
  "Factory Info": {
    "Vendor": "Steinberg Media Technologies",
    "URL": "http://www.steinberg.net",
    "E-Mail": "mailto:info@steinberg.de",
    "Flags": {
      "Unicode": true,
      "Classes Discardable": false,
      "Component Non Discardable": false,
    },
  },
  "Classes": [
    {
      "CID": "BD58B550F9E5634E9D2EFF39EA0927B1",
      "Category": "Audio Module Class",
      "Name": "Hello World",
      "Vendor": "Steinberg Media Technologies",
      "Version": "1.0.0.1",
      "SDKVersion": "VST 3.7.5",
      "Sub Categories": [
        "Fx",
      ],
      "Class Flags": 1,
      "Cardinality": 2147483647,
      "Snapshots": [
      ],
    },
    {
      "CID": "A0B1A6F4005D9B47967177E37A671891",
      "Category": "Component Controller Class",
      "Name": "Hello WorldController",
      "Vendor": "Steinberg Media Technologies",
      "Version": "1.0.0.1",
      "SDKVersion": "VST 3.7.5",
      "Class Flags": 0,
      "Cardinality": 2147483647,
      "Snapshots": [
      ],
    },
  ],
  "Compatibility": [
    {
		"New": "BD58B550F9E5634E9D2EFF39EA0927B1",
		"Old": [
		  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
		  "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
		],
	},
  ],
}
```