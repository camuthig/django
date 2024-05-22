import warnings

from django.core.exceptions import FullResultSet
from django.db.models import Aggregate
from django.db.models.expressions import OrderByList
from django.utils.deprecation import RemovedInDjango60Warning


class OrderableAggMixin(Aggregate):
    allow_order_by = True

    def __init__(self, *expressions, ordering=(), **extra):
        if ordering:
            warnings.warn(
                "The ordering argument is deprecated. Use order_by instead.",
                category=RemovedInDjango60Warning,
            )
            extra["order_by"] = ordering
        if not ordering:
            self.order_by = None
        elif isinstance(ordering, (list, tuple)):
            self.order_by = OrderByList(*ordering)
        else:
            self.order_by = OrderByList(ordering)
        super().__init__(*expressions, **extra)
