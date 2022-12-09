from rest_framework import serializers
from api.models import TcrRequest, PDB_CHOICES, FUNCTION_CHOICES

class TcrRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pdb = serializers.ChoiceField(choices=PDB_CHOICES, default="python")
    action1 = serializers.ChoiceField(choices=FUNCTION_CHOICES, default="python")
    action2 = serializers.ChoiceField(choices=FUNCTION_CHOICES, default="python")
    action3 = serializers.ChoiceField(choices=FUNCTION_CHOICES, default="python")

    def create(self, validated_data):
        return TcrRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pdb = validated_data.get('pdb', instance.pdb)
        instance.action1 = validated_data.get('action1', instance.action1)
        instance.action2 = validated_data.get('action2', instance.action2)
        instance.action3 = validated_data.get('action3', instance.action3)

    class Meta:
        model = TcrRequest
        fields = ('pk', 'pdb', 'action1', 'action2', 'action3')
