from polls.models import User

class UserRepository:

    def get(self):
        return User.objects.all()
    
    def getByCondition(self, **kwargs):
        return User.objects.filter(**kwargs)
    
    def save(self, **kwargs):
        return User.objects.create(**kwargs)
    
    def update(self, instance: User, **kwargs):
        for field, val in kwargs.items():
            setattr(instance, field, val)
        instance.save()
        return instance

    def delete(self, instance: User):
        instance.delete();