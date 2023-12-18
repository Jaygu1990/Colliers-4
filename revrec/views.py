from django.shortcuts import render, get_object_or_404
from .models import revrecmodel
from revrec.uploadrevrec import process_excel_file
from revrec.forms import uploadrevrecform

def revrecview(request):
    revrecdetails = revrecmodel.objects.order_by('name')

    test_list = []
    for revrecdetail in revrecdetails:
        if revrecdetail.test_status != 'tested':
            test_list.append(revrecdetail)
    return render(request, 'revrec/revrec.html', {'revrecs': test_list})

def tested(request):
    revrecdetails = revrecmodel.objects.order_by('name')

    test_list = []
    for revrecdetail in revrecdetails:
        if revrecdetail.test_status == 'tested':
            test_list.append(revrecdetail)
    return render(request, 'revrec/revrectested.html', {'revrecs': test_list})

def revrecupdate(request,deal):
    revrecdetail = get_object_or_404(revrecmodel, deal=deal)
    if revrecdetail.assign_status == 'assigned':
        revrecdetail.assign_status = 'unassigned'
    elif revrecdetail.assign_status == 'unassigned':
        revrecdetail.assign_status = 'assigned'
    revrecdetail.save()

    return render(request, 'revrec/revrec.html', {})

def testupdate(request,deal):
    revrecdetail = get_object_or_404(revrecmodel, deal=deal)
    if revrecdetail.test_status == 'tested':
        revrecdetail.test_status = 'untested'
    elif revrecdetail.test_status == 'untested':
        revrecdetail.test_status = 'tested'
    revrecdetail.save()

    return render(request, 'revrec/revrec.html', {})

def noteupdate(request,deal):
    revrecdetail = get_object_or_404(revrecmodel, deal=deal)

    if request.method == 'POST':
        revrecdetail.note = request.POST.get('value')
        revrecdetail.save()

    return render(request, 'revrec/revrec.html', {})


def uploadrevrec(request):
    if request.method == 'POST':
        form = uploadrevrecform(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']

            success, message = process_excel_file(excel_file)

            if success:
                return render(request, 'revrec.html', {})
            else:
                return render(request, 'revrec.html', {})

    else:
        form = uploadrevrecform()

    return render(request, 'revrec/uploadrevrec.html', {'revrecform': form})