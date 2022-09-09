class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __eq__(self, other):
        return (self.type, self.value) == (other.type, other.value)

    def __str__(self):
        return str((self.type, self.value))

    def __repr__(self):
        return repr((self.type, self.value))
