from .models import Student, Group
from django.db.models import CharField, Value


def members_in_group():

    group_query = Group.objects.all().values().annotate(members=Value('None', output_field=CharField()))
    stude_query = Student.objects.all()

    group_id_list = dict()

    for obj in group_query: group_id_list[obj['group_num']] = []

    for obj in stude_query: group_id_list[str(obj.in_group)].append(obj.name)

    for obj in group_query: obj['members'] = group_id_list[obj['group_num']]

    return group_query
