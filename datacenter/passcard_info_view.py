from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    # print(visits)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visit = {
            'entered_at': f'{visit.format_duration(visit.entered_at)}',
            'duration': f'{visit.format_duration(visit.get_duration(visit))}',
            'is_strange': visit.is_visit_long(visit.get_duration(visit), 20)
        }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
