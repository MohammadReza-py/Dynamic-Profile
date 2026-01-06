# Profile Serializer
from django.apps import apps
from django.db import models

class Serializer():
    def __init__(self, model, userID):
        self.MyModel: models.Model = apps.get_model(model.model_app, model.model_name)
        self.recordObj: models.Model = self.MyModel.objects.values().filter(user=userID)

    def getFields(self):
        fields = self.MyModel._meta.get_fields()
        return fields

    def getModel(self, app, name):
        model = apps.get_model(app, name)
        return model

    def getRecord(self, id):
        return self.recordObj.objects.filter(id=id)

    def serializedData(self):
        returnObj = {}
        for i in range(len(self.recordObj)):
            j = self.recordObj[i]
            returnObj.update({i: j})
        return returnObj


# create a model as Profile with following fields
#    title = models.CharField(max_length=100, null=True, blank=True)
#    fa_title = models.CharField(max_length=100, null=True, blank=True)
#    model_app = models.CharField(max_length=100, null=True, blank=True)
#    model_name = models.CharField(max_length=100, null=True, blank=True)

# Use it in view by following codes;
# field = Profile.objects.filter(title=title).first()
# serializer = profile_serializer.Serializer(field, request.user.id)
