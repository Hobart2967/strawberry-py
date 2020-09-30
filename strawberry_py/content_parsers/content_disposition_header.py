class ContentDispositionHeader:
    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        self._type = value

    @property
    def attributes(self) -> dict:
        return self._attributes

    @attributes.setter
    def attributes(self, value: dict) -> None:
        self._attributes = value

    def __init__(self, header_value):
        super().__init__()
        self._header_value = header_value
        self._attributes = {}
        self.parse_information()

    def parse_information(self):
        items = self._header_value.split(';')
        self._type = items[0]
        for item in items[1:]:
            item_pair = item.strip(' ').split('=')
            self._attributes[item_pair[0]] = item_pair[1].strip("\"")

