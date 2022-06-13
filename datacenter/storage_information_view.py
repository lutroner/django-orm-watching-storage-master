from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits_serialized = []
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits:
        current_visitor = {
            'who_entered': f'{visit.passcard}',
            'entered_at': f'{visit.format_duration(visit.entered_at)}',
            'duration': visit.format_duration(visit.get_duration(visit))
        }
        non_closed_visits_serialized.append(current_visitor)

    context = {
        'non_closed_visits': non_closed_visits_serialized,
    }
    return render(request, 'storage_information.html', context)
