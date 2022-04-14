>/ [VST Home](../) / [VST 3 Licensing](../VST+3+Licensing/Index.md)
>
># Which files fall under which license?

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Licensing](../VST+3+Licensing/Index.md)

---

## Which files of the VST 3 SDK fall under which license?

All files describing the VST 3 interface, except VST 2 files, located in the folder *"pluginterfaces"* of the SDK, fall under the dual-license described previously.

Each of these files includes this text:

``` c++
//----------------------------------------------------------------------------
// This file is part of a Steinberg SDK. It is subject to thelicense terms
// in the LICENSE file found in the top-level directory ofthis distribution
// and at www.steinberg.net/sdklicenses.
// No part of the SDK, including this file, may be copied, modified, propagated,
// or distributed except according to the terms contained inthe LICENSE file.
//----------------------------------------------------------------------------
```

- for all other files of the VST 3 SDK, the respective embedded license text is applicable, for example:
  - all **VSTGUI** files fall under a **BSD style** license
  - all **Helper files** (included in base and public.sdk folders) except VST 2 files fall under a **BSD style** license
  - all **VST 2 files** (included in pluginterfaces and public.sdk folders) fall under the "**Proprietary Steinberg VST 2**" license
  - all **mda-vst3 examples** (*public.sdk/samples/mda-vst3 folder*) fall under a **BSD style** license: Copyright (c) 2008 Paul Kellett

## What about VST 2?

The "Proprietary Steinberg VST 2" license, which is the VST 2 license agreement, allows you to distribute your VST 2 plug-in/host in a binary form. However, please note the following requirements:

- You need written permission from Steinberg Media Technologies GmbH in order to distribute your VST 2 plug-in/host (which had to be done before October 2018).
- You need to mention **Steinberg Media Technologies GmbH** in the about box and/or documentation of your VST 2 plug-in/host and follow the [Steinberg VST usage guidelines](../VST+3+Licensing/Usage+guidelines.md).
- Note that the "Proprietary Steinberg VST 3" license does not include the "Proprietary Steinberg VST 2" license, you have to sign it separately! It was available in the VST 2 SDK and in the VST 3 SDK old version.
- Note that from the first of October 2018, Steinberg does **not accept any more submissions of license agreement for VST 2** plug-in/host! This means:

>If you do not have a license agreement signed with Steinberg before October 2018, you are not allowed to distribute VST 2 plug-ins or VST 2 hosts!
