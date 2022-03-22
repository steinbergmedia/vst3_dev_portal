>/ ... / [VST Module Architecture](../VST+Module+Architecture/Index.md)
>
># Interface Versions and Inheritance

**Related pages:**

- [VST Module Architecture](../VST+Module+Architecture/Index.md)
- [How to derive a class from an interface](../VST+Module+Architecture/Derive+From+Interface.md)

---

Unlike C++ classes, **VST-MA** interfaces do not use inheritance to express specializations of objects. Usually all interfaces are derived from FUnknown. This is because interfaces must **never** change after they have been released. The VST Module Architecture Interfaces use inheritance only for versioning! All specializations will be modeled as separate interfaces!

For example the C++ classes:

    class Shape
    {
    public:
        void setPosition (long x, long y);
    protected:
        long x;
        long y;
    };
    class Rect : public Shape
    {
    public:
        void setDimension (long width, long height);
    protected:
        long width;
        long height;
    };

expressed in **VST-MA**, define an interface for each inheritance level:

    class IShape : public FUnknown
    {
    public:
        virtual void setPosition (long x, long y) = 0;
    };
    class IRect : public FUnknown
    {
    public:
        virtual void setDimension (long width, long height) = 0;
    };

In the next program version there need to be changes to the *Shape* class that look like this:

    class Shape
    {
    public:
        void setPosition (long x, long y);
        void setColor (Color color);
    protected:
        long x;
        long y;
        Color color;
    };

The **VST-MA** representation now reflect the changes to Shape by adding a new interface that inherits from *IShape* and looks like the following code, while the former interface definitions remain the same:

    class IShape2 : public IShape
    {
    public:
        virtual void setColor (Color color) = 0;
    };