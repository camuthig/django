from django.contrib.postgres.fields import ArrayField
from django.db.models import Aggregate, BooleanField, JSONField, TextField, Value

__all__ = [
    "ArrayAgg",
    "BitAnd",
    "BitOr",
    "BitXor",
    "BoolAnd",
    "BoolOr",
    "JSONBAgg",
    "StringAgg",
]


class ArrayAgg(Aggregate):
    function = "ARRAY_AGG"
    allow_distinct = True
    allow_ordering = True

    def __init__(self, *expressions, ordering=(), **extra):
        # Ordering is supported for backwards compatibility and should be deprecated
        # in favor of the order_by argument.
        super().__init__(*expressions, order_by=ordering, **extra)

    @property
    def output_field(self):
        return ArrayField(self.source_expressions[0].output_field)


class BitAnd(Aggregate):
    function = "BIT_AND"


class BitOr(Aggregate):
    function = "BIT_OR"


class BitXor(Aggregate):
    function = "BIT_XOR"


class BoolAnd(Aggregate):
    function = "BOOL_AND"
    output_field = BooleanField()


class BoolOr(Aggregate):
    function = "BOOL_OR"
    output_field = BooleanField()


class JSONBAgg(Aggregate):
    function = "JSONB_AGG"
    allow_distinct = True
    allow_ordering = True
    output_field = JSONField()

    def __init__(self, *expressions, ordering=(), **extra):
        # Ordering is supported for backwards compatibility and should be deprecated
        # in favor of the order_by argument.
        super().__init__(*expressions, order_by=ordering, **extra)


class StringAgg(Aggregate):
    function = "STRING_AGG"
    allow_distinct = True
    allow_ordering = True
    output_field = TextField()

    def __init__(self, expression, delimiter, ordering=(), **extra):
        delimiter_expr = Value(str(delimiter))
        super().__init__(expression, delimiter_expr, order_by=ordering, **extra)
