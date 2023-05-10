>[VST Home](../) / [What is VST?](Index.md)
>
># Use cases

**On this page:**

[[_TOC_]]

**Related pages:**

- [Main benefits of VST 3](../Main+benefits+of+VST+3/Index.md)

---

## Why use VST 3 SDK?

There are different use cases you can realize by using the **VST 3 SDK**:

1. You are a ***plug-in developer*** and you want to create audio FX or instrument plug-ins which can be included and used in a **VST 3** host application.

   - an audio FX plug-in is an audio processor effect taking audio as input and creating audio as output: such as *Delay*, *Phaser*, *Compressor*, *Reverb*, …
   - an instrument plug-in is a sound/audio generator, taking as input note events and creating audio as output: such as emulations of well-known hardware synths. There are 2 kinds of instrument plug-ins: virtual sample-based (using audio samples as the basis for sound generation) and virtual synth (using different types of synthesis: physical modelling, additive, subtractive, FM, sample-based, …)

2. You are a ***host developer*** and you want to load in your application **VST 3** plug-ins:

    - audio FX and/or
    - instruments plug-ins.

## Advantages of using VST 3 SDK

By using **VST 3 SDK** directly:

- you are sure to be compliant with the **VST 3** format.
- developing your plug-in based on the **VST 3** format allows you to support easily new **VST 3** features that improve the integration of these plug-ins inside a DAW. Some 3rd party SDKs use only a common layer between all plug-in formats, limiting in this way the possibility for a better integration, for example exclusive **VST 3** features:
  - [context menu](../Technical+Documentation/Change+History/3.5.0/IComponentHandler3.md)
  - [dirty state](../Technical+Documentation/Change+History/3.1.0/IComponentHandler2.md)
  - loading differentially a preset or a project
  - [note expression](../Technical+Documentation/Change+History/3.5.0/INoteExpressionController.md)
  - see [other benefits of VST 3](../Main+benefits+of+VST+3/Index.md)
- you get optimal integration of the **[VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md)** tool with **VST 3**
- it includes the major plug-in format wrappers: **AAX**, **AUv3**, **AU**, **VST 2** (deprecated)
- the included [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line) allows you to check your plug-in's conformity to the **VST 3** standard

## Examples of VST 3 host applications (05/10/2023)

| **Name**                | **Companies**                     | **Link**                                      |
| ----------------------- | --------------------------------- | --------------------------------------------- |
| ACID Pro                | MAGIX Software GmbH               | <https://www.magix.com>                       |
| Acoustica	              | Acon Digital                      | <https://acondigital.com>                     |
| Audacity                | Audacity Team                     | <https://www.audacityteam.org>                 |
| Audition                | Adobe                        	    | <https://www.adobe.com>                       |
| Bidule                  | Plogue Art et Technologie, Inc.   | <https://www.plogue.com>                      |
| Bitwig                  | Bitwig GmbH                       | <https://www.bitwig.com>                      |
| Camelot                 | Audio Modeling                    | <https://audiomodeling.com>                   |
| Cantabile               | Topten Software                   | <https://www.cantabilesoftware.com>           |
| Catalyst                | Toneworks                         | <https://toneworks.io/>                       |
| Cross DJ                | MixVibes                          | <https://www.mixvibes.com>                    |
| Cubase                  | Steinberg Media Technologies GmbH | <https://new.steinberg.net/cubase>            |
| DaVinci Resolve         | Blackmagic Design                 | <https://www.blackmagicdesign.com/products/davinciresolve>|
| Decibel                 | Process Audio                     | <https://process.audio>                       |
| deCoda                  | zplane                            | <https://products.zplane.de/products/decoda>  |
| Digital Performer	      | MOTU                              | <https://motu.com/en-us/products/software/dp> |
| Dime                    | time offaudio                     | <https://timeoff.audio>                       |
| Dorico                  | Steinberg Media Technologies GmbH | <https://new.steinberg.net/dorico>            |
| Entonal Studio          | Node Audio                        | <https://entonal.studio>                      |
| FL Studio	              | ImageLine                         | <https://www.image-line.com>                  |
| Fluid Chords            | Pitch Innovations                 | <https://www.pitchinnovations.com>            |
| Freestyle Suite         | New Sonic Arts                    | <https://www.newsonicarts.com>                |
| Gig Performer           | Deskew Technologies               | <https://gigperformer.com>                    |
| Komplete Kontrol        | Vienna Symphonic Library GmbH     | <https://www.native-instruments.com>          |
| KSHMR Chain             | Excite Audio                      | <https://www.excite-audio.com>                |
| Live                    | Ableton AG                        | <https://www.ableton.com/en/live>             |
| Maschine                | Native Instruments                | <https://www.native-instruments.com>          |
| Max                     | Cycling 74                        | <https://cycling74.com>                       |
| Metro                   | Sagan Technology                  | <https://sagantech.com>                       |
| Mixcraft                | Acoustica                         | <https://acoustica.com>                       |
| MultitrackStudio        | Bremmers Audio Design             | <https://www.multitrackstudio.com>            |
| Music Maker Plus        | MAGIX Software GmbH               | <https://www.magix.com>                       |
| Nuendo                  | Steinberg Media Technologies GmbH	| <https://new.steinberg.net/nuendo>            |
| Orb Composer Pro        | Hexachords                        | <https://hexachords.com>                      |
| Overture                | Sonic Scores                      | <https://sonicscores.com>                     |
| OwlPlug                 | OwlPlug                           | <https://owlplug.com>                         |
| Qtractor                | rncbc                             | <https://qtractor.org>                        |
| Reaper                  | Reaper                            | <https://www.reaper.fm>                       |
| Reason +                | Reason Studios                    | <https://reasonstudios.com>                   |
| Re:Cycle                | Digital Brain Instruments         | <https://www.digitalbrain-instruments.com>    |
| RipX DeepAudio          | Hit’n’Mix Ltd                     | <https://hitnmix.com>                         |
| Samplitude              | MAGIX Software GmbH               | <https://www.magix.com>                       |
| Serato Studio 2         | Serato                            | <https://serato.com>                          |
| Sonar                   | Bandlab/Cakewalk                  | <https://www.bandlab.com/products/cakewalk>   |
| Sound Forge Audio Studio| MAGIX Software GmbH               | <https://www.magix.com>                       |
| Sound Trajectory 2      | TripinLab                         | <https://www.tripinlab.com>                   |
| Soundop                 | Ivosight Software Inc.            | <https://ivosight.com>                        |
| SpectraLayers           | Steinberg Media Technologies GmbH | <https://www.steinberg.net/spectralayers>     |
| Studio One              | PreSonus Software Ltd             | <https://www.presonus.com/products/Studio-One>|
| Superplugin             | DDMF                              | <https://ddmf.eu>                             |
| TS2                     | Ircam Lab                         | <https://www.ircamlab.com>                    |
| Vienna MIR PRO 3D       | Vienna Symphonic Library GmbH     | <https://www.vsl.co.at>                       |
| VoxPat Pro              | Digital Brain Instruments         | <https://www.digitalbrain-instruments.com/>   |
| VST Live                | Steinberg Media Technologies GmbH | <https://www.steinberg.net/vst-live>          |
| VST Rack Pro            | Yamaha Corporation                | <https://europe.yamaha.com/en/products/proaudio/software/vst_rack/index.html>|
| Waveform                | Tracktion Software Corporation    | <https://www.tracktion.com>                   |
| Wavelab                 | Steinberg Media Technologies GmbH | <https://new.steinberg.net/wavelab>           |
| Zrythm DAW              | Zrythm                            | <https://www.zrythm.org>                      |

