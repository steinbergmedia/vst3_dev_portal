>/ ... / [VST Module Architecture](Index.md)
>
># How the host will load a VST-MA based Plug-in

**Related pages:**

- [VST Module Architecture](Index.md)

---

Check the included cpp files showing how to load such Component/plug-in:

- *public.sdk/source/vst/hosting/module.h*\
and
- *for each platform public.sdk/source/vst/hosting/module_win32.cpp, ...*

Here below you could found a basic implementation on Windows showing how to load the library and get pointer to the wanted exported functions:

``` c++
HMODULE hModule = LoadLibrary ("SomePlugin.dll");
if (hModule)
{
    InitModuleProc initProc = (InitModuleProc)GetProcAddress (hModule, "InitDll");
    if (initProc) // this entry function is optional on Windows, not on MacOS and Linux!
    {
        if (initProc () == false)
        {
            FreeLibrary (module);
            return false;
        }
    }

    GetFactoryProc proc = (GetFactoryProc)GetProcAddress (hModule, "GetPluginFactory");

    IPluginFactory* factory = proc ? proc () : nullptr;
    if (factory)
    {
        for (int32 i = 0; i < factory->countClasses (); i++)
        {
            PClassInfo ci;
            factory->getClassInfo (i, &ci);

            FUnknown* obj;
            factory->createInstance (ci.cid, FUnknown::iid, (void**)&obj);
            ...
            obj->release ();
        }

        factory->release ();
    }

    ExitModuleProc exitProc = (ExitModuleProc)GetProcAddress (hModule, "ExitDll");
    if (exitProc) // This exit function is optional on Windows, not on MacOS and Linux!
        exitProc ();

    FreeLibrary (hModule);
}
```
