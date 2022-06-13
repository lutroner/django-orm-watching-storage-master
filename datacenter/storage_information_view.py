from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timezone, datetime, timedelta


def get_duration(visit):
    return localtime(localtime(datetime.now(timezone.utc))) - localtime(visit.entered_at)


def format_duration(duration):
    if isinstance(duration, timedelta):
        return f'{int(duration.total_seconds() // 3600)}ч. {(duration.seconds // 60) % 60}м.'
    return duration.strftime("%d-%m-%Y, %H:%M:%S")


def storage_information_view(request):
    non_closed_visits_serialized = []
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits:
        current_visitor = {
            'who_entered': f'{visit.passcard}',
            'entered_at': f'{format_duration(visit.entered_at)}',
            'duration': format_duration(get_duration(visit))
        }
        non_closed_visits_serialized.append(current_visitor)

    context = {
        'non_closed_visits': non_closed_visits_serialized,
    }
    return render(request, 'storage_information.html', context)
