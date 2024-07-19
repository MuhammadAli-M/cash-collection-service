from django.conf import settings

from domains.collection.entities.task import Money, BaseEntity

UserID = int


class Collector(BaseEntity):
    amount: Money
    user_id: UserID

    def increment_amount(self, increase):
        self.amount += increase

    def does_amount_above_freeze_limit(self):
        return self.amount >= settings.COLLECTION_FREEZE_AMOUNT
