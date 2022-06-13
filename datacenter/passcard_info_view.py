from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    current_passcard = Passcard.objects.get(passcode=passcode)
    current_passcard_visits = Visit.objects.filter(passcard=current_passcard)
    current_passcard_visits_serialized = []
    for visit in current_passcard_visits:
        this_passcard_visit = {
            'entered_at': f'{visit.format_duration(visit.entered_at)}',
            'duration': f'{visit.format_duration(visit.get_duration(visit))}',
            'is_strange': visit.is_visit_long(visit.get_duration(visit), 20)
        }
        current_passcard_visits_serialized.append(this_passcard_visit)
    context = {
        'passcard': current_passcard,
        'this_passcard_visits': current_passcard_visits_serialized
    }
    return render(request, 'passcard_info.html', context)