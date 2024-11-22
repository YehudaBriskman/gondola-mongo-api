from ariadne import ScalarType
from graphql.language import ast

latitude_scalar = ScalarType("Latitude")
quality_scalar = ScalarType("Quality")
priority_scalar = ScalarType("Priority")
angle_scalar = ScalarType("Angle")
longitude_scalar = ScalarType("Longitude")
nonnegative_float_scalar = ScalarType("NonnegativeFloat")


# Helper function to validate numbers
def is_number(value):
    return isinstance(value, (int, float))


@latitude_scalar.serializer
@latitude_scalar.value_parser
def parse_latitude(value):
    if not is_number(value):
        raise TypeError("Latitude must be a number.")
    if not (-90 <= value <= 90):
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    return value


@latitude_scalar.literal_parser
def parse_latitude_literal(ast_node, variables=None):
    if isinstance(ast_node, (ast.FloatValueNode, ast.IntValueNode)):
        return parse_latitude(float(ast_node.value))
    raise TypeError("Latitude must be a numeric value.")


@longitude_scalar.serializer
@longitude_scalar.value_parser
def parse_longitude(value):
    if not is_number(value):
        raise TypeError("Longitude must be a number.")
    if not (-180 <= value <= 180):
        raise ValueError("Longitude must be between -180 and 180 degrees.")
    return value


@longitude_scalar.literal_parser
def parse_longitude_literal(ast_node, variables=None):
    if isinstance(ast_node, (ast.FloatValueNode, ast.IntValueNode)):
        return parse_longitude(float(ast_node.value))
    raise TypeError("Longitude must be a numeric value.")


@angle_scalar.serializer
@angle_scalar.value_parser
def parse_angle(value):
    if not is_number(value):
        raise TypeError("Angle must be a number.")
    if not (-360 <= value < 360):
        raise ValueError("Angle must be between -360 (inclusive) and 360 (exclusive) degrees.")
    return value


@angle_scalar.literal_parser
def parse_angle_literal(ast_node, variables=None):
    if isinstance(ast_node, (ast.FloatValueNode, ast.IntValueNode)):
        return parse_angle(float(ast_node.value))
    raise TypeError("Angle must be a numeric value.")


@nonnegative_float_scalar.serializer
@nonnegative_float_scalar.value_parser
def parse_nonnegative_float(value):
    if not is_number(value):
        raise TypeError("NonnegativeFloat must be a number.")
    if value < 0:
        raise ValueError("NonnegativeFloat must be a non-negative number.")
    return value


@nonnegative_float_scalar.literal_parser
def parse_nonnegative_float_literal(ast_node, variables=None):
    if isinstance(ast_node, (ast.FloatValueNode, ast.IntValueNode)):
        return parse_nonnegative_float(float(ast_node.value))
    raise TypeError("NonnegativeFloat must be a numeric value.")


@priority_scalar.serializer
@priority_scalar.value_parser
def parse_priority(value):
    if not isinstance(value, int):
        raise TypeError("Priority must be an integer.")
    if not (1 <= value <= 5):
        raise ValueError("Priority must be between 1 and 5.")
    return value


@priority_scalar.literal_parser
def parse_priority_literal(ast_node, variables=None):
    if isinstance(ast_node, ast.IntValueNode):
        return parse_priority(int(ast_node.value))
    raise TypeError("Priority must be an integer value.")


@quality_scalar.serializer
@quality_scalar.value_parser
def parse_quality(value):
    if not isinstance(value, int):
        raise TypeError("Quality must be an integer.")
    if not (0 <= value <= 5):
        raise ValueError("Quality must be between 0 and 5.")
    return value


@quality_scalar.literal_parser
def parse_quality_literal(ast_node, variables=None):
    if isinstance(ast_node, ast.IntValueNode):
        return parse_quality(int(ast_node.value))
    raise TypeError("Quality must be an integer value.")
