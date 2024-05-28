"""
With the builder pattern, we delegate the creation of an object to something other than its constructor. We have more
fine-grained control of the steps used to create an object
"""


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append((name, value))
        return self

    def __str__(self):
        parts = [f"class {self.root_name}:"]
        if not self.fields:
            parts.append("  pass")
        else:
            parts.append("  def __init__(self):")
            parts.extend([f"    self.{name} = {value}" for name, value in self.fields])
        return "\n".join(parts)


class FunctionBuilder:

    def __init__(self, root_name):
        self.root_name = root_name
        self.arguments = []
        self.code = []

    def add_argument(self, name):
        self.arguments.append(name)
        return self

    def add_code_line(self, code):
        self.code.append(code)
        return self

    def __str__(self):
        parts = [f"def {self.root_name} ({", ".join(self.arguments)}):"]
        if not self.code:
            parts.append("  pass")
        else:
            parts.extend([f"  {line}" for line in self.code])
        return "\n".join(parts)


"""
We can use inheritance to extend a builder. This way the original builder remains unchanged, which is in keeping with 
the open-closed principle.
"""


class CodeMethodBuilder(CodeBuilder):
    def __init__(self, root_name):
        CodeBuilder.__init__(self, root_name)
        self.methods = []

    def add_method(self, method):
        self.methods.append(method)
        return self

    def __str__(self):
        ostr = CodeBuilder.__str__(self) + "\n  "
        ostr += "\n".join([str(method).replace("\n", "\n  ") for method in self.methods])
        return ostr
