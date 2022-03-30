>/ [VST Home](/Index.md) / [Frequently Asked Questions](../FAQ/Index.md)
>
># Licensing

[[_TOC_]]

---

## Q: I would like to share the source code of my VST 3 plug-in/host on GitHub or other such platform.

- You can choose the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license and feel free to share your plug-ins/host's source code including or referencing the VST 3 SDK's sources on GitHub.
- You are allowed to provide a binary form of your plug-ins/host too, provided that you provide its source code as [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too.
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/Usage+guidelines.md).

## Q: I would like to distribute my VST 3 plug-in/host as freeware/shareware in binary form only.

- You can distribute your VST 3 plug-in/host in a binary form. This always requires that you to choose the "Proprietary Steinberg VST 3" license.
- Even though you distribute your VST 3 plug-in/host as freeware/shareware you need to adhere to the requirements of the "Proprietary Steinberg VST 3" license. 
- Download the [license agreement](../VST+3+Licensing/What+are+the+licensing+options.md) (it is part of the [SDK](../Getting+Started/Links.md) too), sign it and return it to Steinberg.

## Q: I would like to sell my VST 3 plug-in/host in binary form only.

If you work for-profit and distribute your VST 3 plug-in/host in binary form, you need to choose the "Proprietary Steinberg VST 3" license.
Download the [license agreement](../VST+3+Licensing/What+are+the+licensing+options.md) (it is part of the [SDK](../Getting+Started/Links.md) too), sign it and return it to Steinberg.

## Q: I would like to adapt the VST 3 SDK's sources to my VST 3 plug-in/host's needs.

You can adapt and modify the VST 3 SDK's source for your needs, but if you want to distribute these sources under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) you have to distribute your VST 3 plug-in/host's sources under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too.
It is allowed to modify the VST 3 SDK's when you distribute your VST 3 plug-in/host in binary form and choose the "Proprietary Steinberg VST 3" license.
If you are of the opinion that we should include your changes in the SDK, please contact us (use the [sdk.steinberg.net](https://forums.steinberg.net/c/developer/103/none)).

## Q: I would like to reuse a distributed modified version of the VST 3 SDK for my own VST 3 plug-ins/host.

Yes, but you have to make sure that your VST 3 plug-in/host sources are under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too!

## Q: I would like to distribute my VST 3 plug-in/host in binary form based on a modified version of VST 3 SDK which is under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

- Yes, but you have to make sure that your VST 3 plug-in/host sources are under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too!
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/What+are+the+licensing+options.md).
- If you do not want to be [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html), you have to build your VST 3 plug-in/host based on the original or any private modified version of the VST 3 SDK and choose the "Proprietary Steinberg VST 3" license.

## Q: I would like to sell my VST 3 plug-in/host in binary form which is based on a 3rd party SDK like JUCE.

- If you work for-profit and distribute your plug-in/host in binary form, you need to choose the "Proprietary Steinberg VST3" license.
- Download the [license agreement](../VST+3+Licensing/What+are+the+licensing+options.md) (it is part of the [SDK](../Getting+Started/Links.md) too), sign it and return it to Steinberg.
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/What+are+the+licensing+options.md).

## Q: I would like to distribute my VST 3 plug-in/host in binary form which is based on a 3rd party SDK like JUCE and used its [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

- Yes, but you have to make sure that your VST 3 plug-in/host sources are under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too!
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/What+are+the+licensing+options.md).

## Q: Do I have to sign and send to Steinberg the "Proprietary Steinberg VST 3" license agreement for each new version of the VST 3 SDK?

- No, the license agreement has its own versioning, you just have to be sure that you have already signed the correct version of it.
- As of SDK version **3.6.8**, the license has the version **2.0** (only some minor change/formatting of the text of the license agreement were done in the last SDK versions [3.6.9 up to 3.7.1])
    - **If** you use a **VST 3 SDK version >= 3.6.8**, you have to be sure that you sent Steinberg a signed license agreement (*version 2.x*) from one of the last VST 3 SDKs (>= 3.6.8).
    - **If** you use a **VST 3 SDK version < 3.6.8**, you have to be sure that you sent Steinberg a signed license agreement (**version 1**) included in the VST 3 SDK that you use.
    - **If** you do not know if you already sent it, it is recommended to send it again and in this case it is possible to use the license agreement of the **last VST 3 SDK**, too!
    - **If** you have signed a license agreement (**version 2.x**) and a new released **VST 3 SDK** uses a new license agreement (**version 3.x**), then you have to signed it again.
- The previous explanation also applies to used 3rd parties SDK like JUCE/iPlug/SynthEdit... just check which VST 3 SDK version is used by the 3rd party SDK you work with and sign the correct license agreement or the last available one.

## Q: I would like to share the source code of my VST 2 plug-in/host on GitHub or other web-based exchange platform.

- It is allowed but be sure that you do NOT include the Steinberg VST 2 files: like *aeffect.h* and *aeffectx.h*. These files are under a different license which does not allow redistribution!

## Q: I am a developer/company and I want to develop and distribute a VST 2 plug-in and/or host in binary form.

- If you have signed the VST 2 license agreement (before October 2018), you can.
- If not, you are not allowed to distribute it!
- See [here](../Main+benefits+of+VST+3/Index.html)!