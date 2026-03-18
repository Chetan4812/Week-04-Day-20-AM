class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        combined = tuple(self.components[i] + other.components[i] for i in range(len(self.components)))
        return Vector(combined)

    def __sub__(self, other):
        combined = tuple(self.components[i] - other.components[i] for i in range(len(self.components)))
        return Vector(combined)

    def __mul__(self, scalar):
        multiplied = tuple(x * scalar for x in self.components)
        return Vector(multiplied)

    def __repr__(self):
        return f"Vector{self.components}"

# Testing
v1 = Vector((1, 2))
v2 = Vector((3, 4))
print(v1 + v2)  # Vector(4, 6)
print(v1 * 3)   # Vector(3, 6)
