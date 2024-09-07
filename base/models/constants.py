class Consants:
    NONE = 0
    BUSINESS = 1
    ALL = 2
    VisiblityChoices = (
        (NONE, "None"),
        (BUSINESS, "Business"),
        (ALL, "All"),
    )
    IN_PROCESS = 1
    CONFIRMED = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5
    OrderStatusChoices = (
        (IN_PROCESS, "In Process"),
        (CONFIRMED, "Confirmed"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled"),
    )
