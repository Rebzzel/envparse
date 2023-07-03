class Namespace(object):
    def __init__(self, **attributes):
        self.__dict__.update(**attributes)

    def __repr__(self):
        attrs_repr = []

        for key, value in self.__dict__.items():
            attrs_repr.append("{}={}".format(key, repr(value)))

        return "Namespace({})".format(", ".join(attrs_repr))

    # need for fix lint errors
    def __getattr__(self, key):
        return self.__dict__[key]


__all__ = ["Namespace"]
