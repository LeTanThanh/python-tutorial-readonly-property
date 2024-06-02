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
print(circle.area)

"""
This code works perfectly fine.

But it would be more natural that the area is a property of the Circle object, not a method.
To make the area() method as a property of the Circle class, you can use the @property decorator as follows:

The area is calculated from the redius attribute.
Therefore, it's often called a calculated or computed property.
"""

## Cache calculated properties

"""
Suppose you create a new circle object and access the area property many times.
Each time, the area needs to be recaculated, which is not efficient.

To make it more performant, you need to recalculate the area of the circle only when the redius changes.
If the radius doesn't change, you can reuse the previously calculated area.

To do it, you can use the caching technique:
- First, calculate the area and save it in a cache.
- Second, if the radius changes, reset the area.
Otherwise, return the area directly from the cache without recalculation.

How it works

First, set the _area to None in the __init__ method.
The _area attribute is the cache that stores the calculated area.

Second, if the radius changes (in the setter), reset the _area to None.

Third, define the area computed property.
The area property returns _area if it is not None.
Otherwise, calculate the area, save it into the _area, and return it.
"""
