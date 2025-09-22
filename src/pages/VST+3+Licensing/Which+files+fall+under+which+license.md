>/ [VST Home](../) / [VST 3 Licensing](Index.md)
>
># Which files fall under which license?

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Licensing](Index.md)

---

## Which files of the VST 3 SDK fall under which license?

All files describing the **VST 3** interface, located in the folder *"pluginterfaces"* of the SDK, and all **Helper files** (included in base and public.sdk folders)  fall under the [MIT license](https://tlo.mit.edu/understand-ip/exploring-mit-open-source-license-comprehensive-guide) described previously.

Each of these files includes this text:

``` c++
//----------------------------------------------------------------------------
// This file is part of a Steinberg SDK. It is subject to the license terms
// in the LICENSE file found in the top-level directory of this distribution
// and at www.steinberg.net/sdklicenses.
// No part of the SDK, including this file, may be copied, modified, propagated,
// or distributed except according to the terms contained in the LICENSE file.
//----------------------------------------------------------------------------
```

- for all other files of the **VST 3 SDK**, the respective embedded license text is applicable, for example:
  - all **VSTGUI** files fall under a **BSD style** license
  - all **mda-vst3 examples** (*public.sdk/samples/mda-vst3 folder*) fall under a **BSD style** license: Copyright (c) 2008 Paul Kellett

## What about VST 2?

The "**Proprietary Steinberg VST 2**" license, which is the **VST 2** license agreement, allows you to distribute your **VST 2** plug-in/host in a binary form. However, please note the following requirements:

- You need written permission from Steinberg Media Technologies GmbH in order to distribute your **VST 2** plug-in/host (which had to be done before October 2018).
- You need to mention **Steinberg Media Technologies GmbH** in the about box and/or documentation of your **VST 2** plug-in/host and follow the [Steinberg VST usage guidelines](Usage+guidelines.md).
- Note that from the first of October 2018, Steinberg does **not accept any more submissions of license agreement for VST 2** plug-in/host! This means:

>If you do not have a license agreement signed with Steinberg before **October 2018**, you are not allowed to distribute new **VST 2** plug-ins or **VST 2** hosts!
