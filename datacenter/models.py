from datetime import timedelta, datetime, timezone

from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self, visit):
        if visit.leaved_at:
            return localtime(visit.leaved_at) - localtime(visit.entered_at)
        else:
            return localtime(datetime.now(timezone.utc)) - localtime(visit.entered_at)

    def format_duration(self, duration: datetime):
        if isinstance(duration, timedelta):
            return f'{int(duration.total_seconds() // 3600)}ч. {(duration.seconds // 60) % 60}м.'
        return duration.strftime("%d-%m-%Y, %H:%M:%S")

    def is_visit_long(self, visit, minutes=60):
        if visit < timedelta(minutes=minutes):
            return False
        return True
