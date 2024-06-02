from circle import Circle

# Python Readonly Property

## Introduction to the Python readonly property

"""
To define a readonly property, you need to create a property with only the getter.
However, it is not truly read-only because you can always access the underlying attribute and change it.

The read-only properties are useful in some cases such as for computed properties.

The following example defines a class called Circle that has a radius attribute and an area() method:
"""

circle = Circle(10)
print(circle.area())

"""
This code works perfectly fine.

But it would be more natural that the area is a property of the Circle object, not a method.
To make the area() method as a property of the Circle class, you can use the @property decorator as follows:

The area is calculated from the redius attribute.
Therefore, it's often called a calculated or computed property.
"""
