from domains.collection.entities.task import Money, CollectorID, \
    BaseEntity

UserID = int


class Collector(BaseEntity):
    amount: Money
    user_id: UserID
    is_collected: bool = False
