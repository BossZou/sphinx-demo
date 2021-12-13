class Stub:
    def __init__(self, name):
        """

        :param name: stub name
        """

        #: name of object (docstring of member)
        self._name = name

    def name(self):
        """

        :return: name of object
        """

        return self._name
