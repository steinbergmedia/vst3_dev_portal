>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Clipboard VST-XML

**On this page:**

[[_TOC_]]

---

The **Clipboard VST-XML** format is a simple text-based XML definition used to exchange media-related data through drag and drop or copy and paste.

It was originally designed to support audio file exchange between **Cubase** and **HALion**. Over time, the same mechanism was extended to transfer additional musical elements and their context.

## What It Enables

Clipboard VST-XML allows applications to transfer more than a plain file reference.

Typical transferred elements include:

- Audio files/clips (since version 1.0)
- Tempo (since version 1.1)
- Chords (since version 1.2)
- Scales (since version 1.3)

## Additional Context Data

The XML payload can include extra information that helps preserve editing context across applications and plug-ins, for example:

- Color
- Project time position
- Other element-specific metadata

This makes drag-and-drop and copy-paste workflows more useful than simple file transfer, because the receiving application and plug-ins can reconstruct musical and visual context.

## Typical Workflow

1. A source plug-in like **HALion** serializes the selected element as Clipboard VST-XML text.
2. The user performs drag and drop or copy and paste.
3. The target application like **Cubase** parses the XML and imports the element with its metadata.

## Known applications and plug-ins supporting Clipboard VST-XML

- Cubase
- Dorico
- Nuendo
- HALion
- Padshop
- Studio One
- Soundly
- Wavelab

## Format Description

This section describes the Clipboard VST-XML structure according to its current DTD ([VST-XML-1.4.dtd](../../../resources/VST-XML-1.4.dtd)).

### Root node: `vst-xml`

| Item | Definition |
|---|---|
| Attributes | `version` (required) |
| Required children | `sourceApp` |
| Optional children | `region`, `chord`, `scale`, `signature` |

### Node: `sourceApp`

| Item | Definition |
|---|---|
| Content | Text value with sender application name |

### Node: `region`

| Item | Definition |
|---|---|
| Attributes | `id` (required), `type` (optional: `join` or `silence`), `channelID` (optional) |
| Required children | `filename`, `start`, `end` |
| Optional children | `name`, `tempo`, `rootkey`,  `projectTime`, `color`, `loop`, `segment`, `signature` |

### Node: `segment`

| Item | Definition |
|---|---|
| Required children | `filename`, `start`, `length` |
| Optional children | `fileOffset` |

### Node: `loop`

| Item | Definition |
|---|---|
| Attributes | `type` (optional: `release`) |
| Required children | `start`, `end` |

### Node: `chord`

| Item | Definition |
|---|---|
| Attributes | `id` (required) |
| Required children | `keyNote`, `pitches`, `mask` |
| Optional children | `name`, `projectTime`, `bassNote`, `color` |

### Node: `scale`

| Item | Definition |
|---|---|
| Attributes | `id` (required) |
| Required children | `mask`, `keyNote` |
| Optional children | `name`, `projectTime`, `displayName`, `color` |

### Node: `signature`

| Item | Definition |
|---|---|
| Required children | `numerator`, `denominator` |
| Optional children | `projectTime` |

### Leaf tag meanings

| Tag | Meaning |
|---|---|
| `name` | Human-readable label |
| `displayName` | Alternate/display label for scale |
| `filename` | Audio file path |
| `start` | Start position or offset (context dependent) |
| `end` | End position (context dependent) |
| `length` | Segment length |
| `fileOffset` | File offset used by segment-based payloads |
| `projectTime` | Timeline position; requires `domain` attribute |
| `tempo` | Tempo value |
| `rootkey` | Root key value |
| `pitches` | Chord pitch set as text |
| `keyNote` | Chord/scale key note value |
| `bassNote` | Chord bass note value |
| `mask` | Bitmask-like harmonic/scale encoding |
| `color` | Color value (for UI/context) |
| `numerator` | Time signature numerator |
| `denominator` | Time signature denominator |

### Attribute reference

| Attribute | Used on | Values |
|---|---|---|
| `id` | `region`, `chord`, `scale` | Any text (like integer counter), required |
| `type` | `region` | `join`, `silence` |
| `type` | `loop` | `release` |
| `channelID` | `region` | Any text (typically GUID) |
| `domain` | `projectTime` | `quarterNotes` or `seconds` (required) |

## Examples of Clipboard VST-XML

### Insert one audio file at position beat 16

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <sourceApp>MyApp</sourceApp>
    <region id="1" channelID="{B48CE04A-8FE5-4192-BBEE-D178F7B55C26}">
        <name>Region 1</name>
        <filename>c:\toto.wav</filename>
        <start>100</start>
        <end>44200</end>
        <projectTime domain="quarterNotes">16</projectTime>
    </region>
</vst-xml>
```

### Insert one audio file at 4s and one audio file at beat 8 on two different tracks

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <sourceApp>MyApp</sourceApp>
    <region id="1" channelID="{B48CE04A-8FE5-4192-BBEE-D178F7B55C26}">
        <name>Region 1</name>
        <filename>E:\Temp\Audio\Drum1.wav</filename>
        <start>100</start>
        <end>44200</end>
        <projectTime domain="seconds">4.0</projectTime>
        <color>#91959bff</color>
    </region>
    <region id="2" channelID="{09FCC4AB-1752-4A8B-A039-380B6EE74256}">
        <name>Region 2</name>
        <filename>E:\Temp\Audio\Drum2.wav</filename>
        <start>0</start>
        <end>44100</end>
        <projectTime domain="quarterNotes">8</projectTime>
        <color>#91959bff</color>
    </region>
</vst-xml>
```

### Insert one audio file at 4s and one audio file at beat 8 on one track

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <sourceApp>MyApp</sourceApp>
    <region id="1" channelID="{B48CE04A-8FE5-4192-BBEE-D178F7B55C26}">
        <name>Region 1</name>
        <filename>E:\Temp\Audio\Drum1.wav</filename>
        <start>100</start>
        <end>44200</end>
        <projectTime domain="seconds">4.0</projectTime>
    </region>
    <region id="2" channelID="{B48CE04A-8FE5-4192-BBEE-D178F7B55C26}">
        <name>Region 2</name>
        <filename>E:\Temp\Audio\Drum2.wav</filename>
        <start>0</start>
        <end>44100</end>
        <projectTime domain="quarterNotes">8</projectTime>
    </region>
</vst-xml>
```
### 4 Chords

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <chord id="818292160">
        <name>C7</name>
        <color>#91959bff</color>
        <projectTime domain="quarterNotes">0</projectTime>
        <pitches>C1;E2;G2;A#2;</pitches>
        <keyNote>60</keyNote>
        <bassNote>24</bassNote>
        <mask>0x248</mask>
    </chord>
    <chord id="1485759856">
        <name>Fmin7</name>
        <color>#91959bff</color>
        <projectTime domain="quarterNotes">32</projectTime>
        <pitches>F1;G#2;C3;D#3;</pitches>
        <keyNote>65</keyNote>
        <bassNote>29</bassNote>
        <mask>0x244</mask>
    </chord>
    <chord id="1485760336">
        <name>Esus4</name>
        <color>#91959bff</color>
        <projectTime domain="quarterNotes">56</projectTime>
        <pitches>E1;A2;B2;E3;</pitches>
        <keyNote>64</keyNote>
        <bassNote>28</bassNote>
        <mask>0x50</mask>
    </chord>
    <chord id="1485759376">
        <name>Gsus2</name>
        <color>#91959bff</color>
        <projectTime domain="quarterNotes">72</projectTime>
        <pitches>G1;G2;A2;D3;</pitches>
        <keyNote>67</keyNote>
        <bassNote>31</bassNote>
        <mask>0x42</mask>
    </chord>
    <sourceApp>Nuendo</sourceApp>
</vst-xml>
```

### 2 Scales

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <scale id="492403952">
        <name>Blues 1</name>
        <displayName>A# Blues 1</displayName>
        <color>#91959bff</color>
        <projectTime domain="quarterNotes">0</projectTime>
        <keyNote>10</keyNote>
        <mask>0x6ed</mask>
    </scale>
    <scale id="492405312">
        <name>Major</name>
        <displayName>G Major</displayName>
        <color>#91959bff</color>
        <projectTime domain="quarterNotes">56</projectTime>
        <keyNote>7</keyNote>
        <mask>0xab5</mask>
    </scale>
    <sourceApp>Nuendo</sourceApp>
</vst-xml>
```

### Signature

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <sourceApp>MyApp</sourceApp>
    <signature>
        <numerator>3</numerator>
        <denominator>4</denominator>
        <projectTime domain="quarterNotes">0</projectTime>
    </signature>
</vst-xml>
```

### Join of segments and loops

``` xml
<?xml version="1.0"?>
<vst-xml version="1.3">
    <sourceApp>WaveLab</sourceApp>
    <region type="join" id="4" channelID="{B48CE04A-8FE5-4192-BBEE-D178F7B55C26}">
        <name>my Region</name>
        <projectTime domain="seconds">33.5</projectTime>
        <segment>
            <filename>E:\Temp\Audio\Drum2.wav</filename>
            <start>0</start>
            <length>1234</length>
        </segment>
        <segment>
            <filename>c:\toto.wav</filename>
            <start>1227</start>
            <length>44</length>
        </segment>
        <color>#12345678</color>
    </region>
    <region id="1234" channelID="{B48CE04A-8FE5-4192-BBEE-D178F7B55C26}">
        <name>Region 1</name>
        <filename>E:\Temp\Audio\Drum2.wav</filename>
        <start>0</start>
        <end>1234</end>
        <projectTime domain="quarterNotes">16</projectTime>
        <loop>
            <start>0</start>
            <end>1002</end>
        </loop>
        <loop type="release">
            <start>0</start>
            <end>1002</end>
        </loop>
        <tempo>120.0</tempo>
        <rootkey>36</rootkey>
        <signature>
            <numerator>3</numerator>
            <denominator>4</denominator>
        </signature>
    </region>
</vst-xml>
```
