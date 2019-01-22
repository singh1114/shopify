class BaseDbIO:
    """Base Db IO class to handle all db operations."""

    def __init__(self, model):
        """Initialize the Base DBIO class."""
        self.model = model

    def get_object(self, kwargs):
        return self.model.objects.get(**kwargs)

    def filter_objects(self, kwargs):
        return self.model.objects.filter(**kwargs)

    def create_object(self, kwargs):
        return self.model.objects.create(**kwargs)

    def update_object(self, model_object, kwargs):
        for key, value in kwargs.items():
            setattr(model_object, key, value)
        return model_object.save()
