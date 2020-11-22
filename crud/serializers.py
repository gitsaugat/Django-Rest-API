from .models import Assignment, Student
from rest_framework import serializers


class AssignmentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    description = serializers.CharField()
    date_added = serializers.DateTimeField()

    def create(self, validated_data):
        return Assignment.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'fname', 'Lname', 'grade', 'admission_date', 'fatherName', 'mothersName', 'studentNumber',
                  'fathersNumber', 'mothersNumber', 'personalEmail', 'schoolEmail']
