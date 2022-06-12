from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timezone, datetime, timedelta


# def get_duration(visit):
#     if visit.leaved_at:
#         return localtime(visit.leaved_at) - localtime(visit.entered_at)
#     else:
#         return localtime(datetime.now(timezone.utc)) - localtime(visit.entered_at)


# def format_duration(duration):
#     if isinstance(duration, timedelta):
#         return f'{int(duration.total_seconds() // 3600)}ч. {(duration.seconds // 60) % 60}м.'
#     return duration.strftime("%d-%m-%Y, %H:%M:%S")


# def is_visit_long(visit, minutes=60):
#     if visit < timedelta(minutes=minutes):
#         return False
#     return True


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
