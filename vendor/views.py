from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from vendor.models import vendorRequest,AXvendor
from vendor.forms import vendorRequestForm,vendorReviewForm,uploadAXvendors
from django.core.files.storage import FileSystemStorage
from vendor.import_excel import process_excel_file
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden
from functools import wraps

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        return wrapped_view
    return decorator


# Create your views here.
def AXvenderSearch(request):
    filter_name = request.GET.get('filter_name', '')
    filter_code = request.GET.get('filter_code', '')
    filter_address = request.GET.get('filter_address', '')

    if not filter_name and not filter_code and not filter_address:
        # If no filters provided, load the first 20 data items, this is to avoid load too much data in the beginning
        AXvendors = AXvendor.objects.all()[:10]
    else:
        AXvendors = AXvendor.objects.filter(
            vendor_name__icontains=filter_name,
            vendor_code__icontains=filter_code,
            vendor_address__icontains=filter_address
        )
    table_html = render_to_string('vendor/vendorSearch.html', {'AXvendors': AXvendors})
    # Return the HTML as a response
    return HttpResponse(table_html)


def pending(request):
    vendor_requests = vendorRequest.objects.order_by("date")
    diction = {'vendor_requests': vendor_requests}
    return render(request, 'vendor/pendingList.html',context= diction)

def reviewing(request):
    review = vendorRequest.objects.order_by("date")
    diction = {'vendor_reviews': review}
    return render(request, 'vendor/reviewingList.html',context= diction)

def createRequest(request):
    form = vendorRequestForm()
    if request.method =="POST":
        form = vendorRequestForm(request.POST,request.FILES)

        if form.is_valid():
            form.instance.status = 'pending for setup'
            form.save(commit=True)
            return pending(request)
        else:
            print("Your form has errors:", form.errors)
    return render(request,'vendor/requestePage.html',{'createForm':form})

@group_required('vendor preparer')
def setRequest(request,deal_number,vendor_name):
    vendor_request = get_object_or_404(vendorRequest, deal_number=deal_number,vendor_name=vendor_name)
    if request.method == 'POST':
        form = vendorReviewForm(request.POST, request.FILES,instance=vendor_request)
        if form.is_valid():
            form.instance.status = 'pending for review'
            form.save()
            return pending(request)
    else:
            form = vendorReviewForm(instance=vendor_request)
    return render(request, 'vendor/setupPage.html', {'setupForm': form})
@group_required('vendor reviewer')
def reviewRequest(request,deal_number,vendor_name):
    vendor_request = get_object_or_404(vendorRequest, deal_number=deal_number,vendor_name=vendor_name)
    if request.method == 'POST':
        form = vendorReviewForm(request.POST,instance=vendor_request)
        if form.is_valid():
            action = request.POST.get('action')
            if action == 'approve':
                form.instance.status = 'finished'
            elif action == 'reject':
                form.instance.status = 'pending for setup'
            form.save()
            return reviewing(request)
    else:
            form = vendorReviewForm(instance=vendor_request)
    return render(request, 'vendor/reviewPage.html', {'reviewForm': form})

@group_required('vendor reviewer')
def upload_excel(request):
    if request.method == 'POST':
        form = uploadAXvendors(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            fs = FileSystemStorage()

            # Ensure unique filenames
            filename = fs.get_available_name(excel_file.name)
            file_path = fs.save(filename, excel_file)

            success, message = process_excel_file(file_path)

            if success:
                return pending(request)
            else:
                return pending(request)

    else:
        form = uploadAXvendors()

    return render(request, 'vendor/uploadAXvendor.html', {'AXform': form})


@group_required('vendor reviewer')
def licensemanagement(request):
    vendor_requests = vendorRequest.objects.order_by("expiration_date")
    diction = {'vendor_license': vendor_requests}
    return render(request, 'vendor/LicenseManagement.html',context= diction)




