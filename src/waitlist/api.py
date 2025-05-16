from ninja import Router
from.schema import *
from .models import WaitlistModel
from typing import List
from django.shortcuts import get_object_or_404

router = Router()

@router.get('', response=List[ListWaitlist])
def listwaitlistentries(request):
    queryset = WaitlistModel.objects.all()
    return queryset


@router.get("{entry_id}", response=WaitlistDetails)
def waitlistentriesdetail(request, entry_id: int):
    queryset = get_object_or_404(WaitlistModel, id=entry_id)
    return queryset
