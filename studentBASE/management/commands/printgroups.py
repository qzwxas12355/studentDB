from django.core.management.base import AppCommand
from django.core.management.base import NoArgsCommand
from optparse import make_option
from studentBASE.models import Group, Student

class Command( NoArgsCommand ):
    help = 'Prints group and student in it.'

    requires_model_validation = True

    def handle_noargs(self, **options):
        lines = []
        list_obj = Group.objects.all()
        for group in list_obj:
            lines.append(group.__str__())
            for student in group.student_set.all():
                lines.append('  ' + student.__str__())
        return "\n".join( lines )