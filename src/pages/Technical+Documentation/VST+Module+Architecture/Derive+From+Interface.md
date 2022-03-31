>/ ... / [VST Module Architecture](../VST+Module+Architecture/Index.md)
>
># Hot to derive a class from an interface

**Related pages:**

- [VST Module Architecture](../VST+Module+Architecture/Index.md)
- [Interface Versions and Inheritance](../VST+Module+Architecture/Interface+Versions+and+Inheritance.md)

---

In the first example we derive a class directly from FUnknown, using some of the helper macros provided by the SDK.

```
class CMyClass: public FUnknown
{
public:
    CMyClass ();
    virtual ~CMyClass ();

    DECLARE_FUNKNOWN_METHODS  // declares queryInterface, addRef and release
};

CMyClass::CMyClass ()
{
    FUNKNOWN_CTOR // init reference counter, increment global object counter
}

CMyClass::~CMyClass ()
{
    FUNKNOWN_DTOR // decrement global object counter
}

IMPLEMENT_REFCOUNT (CMyClass) // implements reference counting

tresult CMyClass::queryInterface (const char* iid, void** obj)
{
    QUERY_INTERFACE (iid, obj, ::FUnknown::iid, CMyClass)
    return kNoInterface;
}
```

Developing a class with more than one interface is done by multiple inheritance. Additionally you have to provide an appropriate cast for each interface in the queryInterface method.

```
class CMyMultiClass : public Steinberg::IPluginBase,
                    public Steinberg::IPlugController,
                    public Steinberg::IEditorFactory
{
public:
    DECLARE_FUNKNOWN_METHODS

    // declare the methods of all inherited interfaces here...
};

IMPLEMENT_REFCOUNT (CMyMultiClass) // implements referencecounting

tresult CMyMultiClass::queryInterface (const char* iid,void** obj)
{
    QUERY_INTERFACE (iid, obj, Steinberg::FUnknown::iid, IPluginBase)
    QUERY_INTERFACE (iid, obj, Steinberg::IPluginBase::iid, IPluginBase)
    QUERY_INTERFACE (iid, obj, Steinberg::IPlugController::iid, IPlugController)
    QUERY_INTERFACE (iid, obj, Steinberg::IEditorFactory::iid, IEditorFactory)
    *obj = 0;
    return kNoInterface;
}
```
