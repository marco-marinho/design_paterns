"""
The façade design pattern uses composition to combine a set of complex objets into a simplified API.

The façade design pattern is a structural pattern that provides a simplified interface to a complex subsystem.
This pattern hides the complexities of the subsystem and provides a unified, higher-level interface that makes
the subsystem easier to use.

Key Points:
1 - Simplified Interface: The façade provides a simple and easy-to-understand interface over a set of interfaces in a
    subsystem, making the subsystem easier to use.
2 - Decoupling: Helps decouple a client from the subsystem, reducing dependencies and making the code more modular.
3 - Unified Access: Facilitates access to complex libraries, frameworks, or APIs by exposing only the necessary
    functionality.

https://refactoring.guru/design-patterns/facade
"""


class BinaryDecoder:

    def read(self, path):
        pass


class Deflater:

    def set_algorithm(self, algorithm):
        pass

    def deflate(self, data):
        pass


class AlgorithmA:
    pass


class AlgorithmB:
    pass


class Validador:

    def validate(self, data):
        pass


class BinaryReader:

    def read(self, path, extension):
        reader = BinaryDecoder()
        data = reader.read(path)
        if extension == "a":
            algorithm = AlgorithmA()
        else:
            algorithm = AlgorithmB()
        deflator.set_algorithm(algorithm)
        deflated_data = deflator.deflate(data)
        validator = Validator()
        if validator.validate(deflated_data):
            return deflated_data
        else:
            raise ValueError
