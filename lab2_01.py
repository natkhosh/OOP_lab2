class A:
    public_class_attr_A = 'public_class_attr_A'
    _protected_class_attr_A = 'protected_class_attr_A'
    __privat_class_attr_A = 'privat_class_attr_A'

    def __init__(self):
        self.public_object_attr_A = 'public_object_attr_A'
        self._protected_object_attr_A = 'protected_object_attr_A'
        self.__privat_object_attr_A = 'privat_class_attr_A'

    @property
    def public_object_method_(self):
        print('public_object_method')
        return self.public_object_attr_A

    @property
    def protected_object_method(self):
        print('protected_object_method')
        return self._protected_object_attr_A

    @property
    def privat_object_method(self):
        print('privat_object_method')
        return self.__privat_object_attr_A

    @staticmethod
    def public_object_method__static():
        print('staticmethod_public_object_method')

    @staticmethod
    def protected_object_method_static():
        print('staticmethod_protected_object_method')

    @staticmethod
    def privat_object_method_static():
        print('staticmethod_privat_object_method')

    @classmethod
    def public_object_method_classmeth(cls):
        print(cls.public_class_attr_A)

    @classmethod
    def protected_object_method_classmeth(cls):
        print(cls._protected_class_attr_A)

    @classmethod
    def privat_object_method_classmeth(cls):
        print(cls.__privat_class_attr_A)

    def public_object_method(self):
        print('privat_object_method')







