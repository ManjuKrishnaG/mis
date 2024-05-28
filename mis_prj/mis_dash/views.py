from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from datetime import date
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.core.mail import send_mail


def validate_refid(refid):
    with connection.cursor() as cursor:
        # Execute a raw SQL query to check if the refid exists in your MySQL table
        cursor.execute("SELECT COUNT(*) FROM user_mas WHERE refid = %s", [refid])
        # Fetch the result of the query
        row = cursor.fetchone()
        # The result will be a tuple with the count of rows matching the refid
        count = row[0]
        # If count is exactly 1, return True
        return count == 1

def get_user_data(refid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT firstname, lastname, empid, location_name, division_name FROM user_mas WHERE refid = %s", [refid])
        row = cursor.fetchone()
        if row:
            firstname, lastname, empid, location_name, division_name = row
            return {'firstname': firstname, 'lastname': lastname, 'empid': empid, 'location_name':location_name, 'division_name':division_name}
        else:
            return None

def delete_data(request):
    if request.method == 'POST':
        # Delete the data from the database
        # For example, if you want to delete the entry for the current date:
        today = date.today()
        title_creation = request.POST.get('title_creation')
        print(title_creation)
        # FormData.objects.filter(date=today).delete()
        return JsonResponse({'message': 'Data deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def change_edit_field(request):
    if request.method == 'POST':
        # Assuming you are passing 'edit' as a parameter in the POST request
        edit_value = request.POST.get('edit', None)
        # Assuming you have a way to identify the FormData object for which you want to change the 'edit' field
        # Here, I'm assuming you have an emp_id and title_creation to identify the object
        refid = request.session.get('refid')
        user_data = get_user_data(refid)
        emp_id = user_data.get('empid')
        
        # Update the FormData object
        try:
            form_data = FormData.objects.filter(empid=emp_id  )
            for data in form_data:
                data.edit = False
                data.save()
            return JsonResponse({'success': True})
        except FormData.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'FormData object does not exist'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
def mis_dashboard(request,refid):
    print(refid)
    user_data = get_user_data(refid)
      
    emp_id = None
    loc = None
    div = None

    if user_data:
        emp_id = user_data.get('empid')
        loc = user_data.get('location_name')
        div = user_data.get('division_name')
        request.session['refid'] = refid


    # Access session data
    
    
    print(div)
    Locations=Show.objects.filter(locations=loc, divisions= div)
    list_values = []

    for location in Locations:
        titles = location.list.all()  # Retrieve all related Title_Creation objects
        for title in titles:
            list_values.append(title.title_creation)  # Access the specific field of Title_Creation
        
# Removing duplicates if needed
    list_values = list(set(list_values))
    print(list_values)
    location = Location.objects.all()
    tc = Title_Creation.objects.filter(title_creation__in=list_values).order_by('-id')  # Reverse order by 'id' or any other suitable field
    print(tc)
    # Reverse the order of tc queryset
    tc = reversed(tc)
    if validate_refid(refid):
        user_data = get_user_data(refid)
        context = {
            'user_data': user_data,
            'refid': refid,
            'emp_id':emp_id,
            'loc':loc,
            'div':div,
            'tc':tc
            
        }
        return render(request, 'mis_dashboard.html', context)
    else:
        return HttpResponse("Invalid refid")

def calender(request):
    titles = Title_Creation.objects.filter(disable=False)
    # form_data = FormData.objects.all()
    context={
        'titles': titles,
        # 'form_data': form_data,

    }
    return render(request, 'calender.html', context)


def adminscrn(request):
    return render(request, 'adminscrn.html')
 
def manage(request):
    refid = request.session.get('refid')
    user_data = get_user_data(refid)
    employees= FormData.objects.all()
    unique_employees = []
    for employee in employees:
    # Check if the employee ID is already in the list of unique employees
        if not any(e.empid == employee.empid for e in unique_employees):
        # Add the employee object to the list if the ID is unique
            unique_employees.append(employee)
    print(unique_employees)
    context={ 'employees':unique_employees }
    return render(request, 'manage.html', context )

def people_trained(request):
    refid = request.session.get('refid')
    user_data = get_user_data(refid)
    emp_id = None
    loc = None
    div = None

    if user_data:
        emp_id = user_data.get('empid')
        loc = user_data.get('location_name')
        div = user_data.get('division_name')

    print(div)
    Locations=Show.objects.filter(locations=loc, divisions= div)
    list_values = []

    for location in Locations:
        titles = location.list.all()  # Retrieve all related Title_Creation objects
        for title in titles:
            list_values.append(title.title_creation)  # Access the specific field of Title_Creation
        
# Removing duplicates if needed
    list_values = list(set(list_values))
    print(list_values)
    location = Location.objects.all()
    tc = Title_Creation.objects.filter(title_creation__in=list_values).order_by('-id')  # Reverse order by 'id' or any other suitable field
    dc = Title_Creation.objects.filter(title_creation__in=list_values).order_by('-id')  # Reverse order by 'id' or any other suitable field
    values = FormData.objects.filter(empid=emp_id)
    print(emp_id)
    print(values)
    # Reverse the order of tc queryset
    tc = reversed(tc)
    return render(request, 'people_trained.html', {'location': location, 'tc': tc,'dc':dc, 'empid':emp_id,'div':div, 'loc':loc,'Locations':Locations, 'values':values})

def save_form_data(request):
    try:
            refid = request.session.get('refid')
            user_data = get_user_data(refid)
            emp_id = None
            location = None
            division = None
            form_number= None
            firstname = None
            if user_data:
                emp_id = user_data.get('empid')
                division= user_data.get('division_name')
                location= user_data.get('location_name')
                firstname= user_data.get('firstname')
            if FormData.objects.filter(location = location).last(): 
                form = FormData.objects.filter(location = location).last()
                form_number = int(form.form_number) + 1
            else:
                form_number = 1
            today = date.today()
            existing_entry = FormData.objects.filter(date__month=today.month, empid=emp_id).first()
            month_start = today.replace(day=1)
            if request.method == 'POST':
                # Iterate over the keys in request.POST to handle each field individually
                for field_name, field_value in request.POST.items():
                    if field_name == 'csrfmiddlewaretoken' or field_name == 'title_creation':
                        continue  # Skip csrfmiddlewaretoken and title_creation fields
                    
                    # Extract title_creation from field_name
                    title_creation, field_name = field_name.split('_', 1)
                    print("Title Creation:", title_creation)
                    print("Field Name:", field_name)
                    print("Field Value:", field_value)

                    # Check if field_value is not null before saving
                    if field_value is not None:
                        # Check if an instance already exists for this empid, title_creation, and field_name
                        form_data, created = FormData.objects.get_or_create(
                            empid=emp_id,
                            title_creation=title_creation,
                            field_name=field_name,
                            division=division,
                            location=location,
                            firstname= firstname,
                        )

                        # Update or create the form data
                        if not created and existing_entry:
                            # If the instance already exists, update its field_value
                            form_data.field_value = field_value
                            month_start = today.replace(day=1)
                            editable = True if 1 <= today.day <= 31 else False
                            if editable:
                                form_data.save()
                            print("Form Data Updated:", form_data)
                        else:
                            # If the instance does not exist, create it with the given field_value
                            form_data.field_value = field_value
                            form_data.form_number= form_number
                            month_start = today.replace(day=1)
                            print(today.day)
                            editable = True if 1 <= today.day <= 31 else False
                            if editable:
                                form_data.save()
                            print("Form Data Created:", form_data)
                    else:
                        print("Field Value is null. Skipping...")

                # You can add any additional logic here
    except IntegrityError as e:
                    # Handle the IntegrityError due to duplication
                    print("Integrity Error:", e)
                    # Add your handling logic here, such as logging the error or informing the user

    return render(request, 'people_trained.html')


def save_data(request):
    if request.method == 'POST':
        title_name = request.POST.get('titleCreation')
        field_name = request.POST.get('fieldCreation')
        division = request.POST.get('division')
        location_name = request.POST.get('location')

        # Create or get Title_Creation instance
        title_creation, created = Title_Creation.objects.get_or_create(title_creation=title_name)

        # Create Field_Creation instance
        field_creation = Field_Creation.objects.create(field=field_name)

        # Add Field_Creation instance to Title_Creation
        title_creation.fields.add(field_creation)

        # Create Location instance
        location = Location.objects.create(location=location_name, Division=division)

        # Add Title_Creation instance to Location
        location.Title_Creation_names.add(title_creation)

        return JsonResponse({'message': 'Data saved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
from django.http import JsonResponse
from .models import Title_Creation, Field_Creation, Location

def get_data(request):
    if request.method == 'GET':
        titles = Title_Creation.objects.all()
        fields = Field_Creation.objects.all()
        divisions = Location.objects.values_list('Division', flat=True).distinct()
        locations = Location.objects.values_list('location', flat=True).distinct()
        data = {
            'titles': list(titles.values('id', 'title_creation')),  # Adjusted to use 'title_creation' instead of 'title'
            'fields': list(fields.values('id', 'field')),
            'divisions': [{'value': division, 'label': division} for division in divisions],
            'locations': [{'value': location, 'label': location} for location in locations],
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def disable_data(request):
    if request.method == 'GET':
        titles = Title_Creation.objects.filter(disable=True)
        
        data = {
            'titles': list(titles.values('id', 'title_creation')),
           
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



def enable_data(request):
    if request.method == 'POST':
        # field = request.POST.get('fieldId')
        # print(field)
        # sub_field_id = request.POST.get('subFieldId')
        # division = request.POST.get('division')
        # location = request.POST.get('location')
        data = json.loads(request.body)
        print(data)

        # Assuming you have a model named YourModel with fields field_id, sub_field_id, division, location, and enabled
        # Fetch the object based on the provided parameters
        data_object = Title_Creation.objects.get(id=data["fieldId"])
        
       
        # Toggle the enabled field
        data_object.disable = not data_object.disable

        data_object.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

import logging

logger = logging.getLogger(__name__)


def update_approval_request(request):
    if request.method == 'POST':
        refid = request.POST.get('refid')
        month = request.POST.get('month')  # Get the selected month
        remarks = request.POST.get('remarks')
        if refid:
            with connection.cursor() as cursor:
                try:
                    # Fetch details from user_mas table where approval status is 1
                    cursor.execute("SELECT * FROM user_mas WHERE approval_st = 1")
                    rows = cursor.fetchall()

                    # Print details to console for each record
                    print("Details of records with approval status 1:")
                    for row in rows:
                        print("Ref ID:", row[0])  # Assuming the first column is refid
                        print("Other details if any:", row[1:])  # Assuming the rest are details

                    # Update approval status for the specific refid
                    sql = "UPDATE user_mas SET approval_st = %s WHERE refid = %s"
                    new_value = True
                    cursor.execute(sql, [new_value, refid])

                    subject = 'Approval Request Updated'
                    message = 'The approval request with refid {} has been updated successfully.'.format(refid)
                    message += f'Selected Month: {month}\n'
                    message += f'Remarks: {remarks}'
                    from_email = 'vandhana.jayakumar1106@gmail.com'  # Update with your email
                    to_email = ['vandhana.jayakumar1106@gmail.com']  # Update with recipient's email
                    send_mail(subject, message, from_email, to_email)

                    ApprovalNotification.objects.create(refid=refid, month=month, remarks=remarks)

                    return JsonResponse({'success': True, 'message': 'Approval request updated successfully'})
                except Exception as e:
                    return JsonResponse({'success': False, 'message': str(e)})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid refid'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


from django.http import JsonResponse
from django.http import JsonResponse
from django.http import JsonResponse
from .models import FormData

def delete_field_values(request):
    print("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    if request.method == 'POST':
        print(request.POST)

        title_creation = request.POST.get('title_creation')
        
        if not title_creation:
            return JsonResponse({'error': 'Title creation parameter is missing or empty'}, status=400)

        try:
            # Assuming you have a model named FormData with fields empid and title_creation
            # Delete all field values associated with the given title_creation
            FormData.objects.filter(title_creation=title_creation).delete()
            return JsonResponse({'message': 'Field values deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while deleting field values', 'detail': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


from django.shortcuts import render, redirect
from .models import Attachment

def upload_files(request):
    refid = request.session.get('refid')
    user_data = get_user_data(refid)
    emp_id = user_data.get('empid')
    division = user_data.get('division_name')
    location = user_data.get('location_name')
    success_message = None

    if request.method == 'POST':
        plan_for_next_month = request.POST.get('plan_for_next_month', '')  # Get the value from the text field
        remarks = request.POST.get('remarks', '')
        today = date.today()

        for file in request.FILES.getlist('attachment'):
            # Check if an attachment with the empid already exists
            try:
                attachment = Attachment.objects.get(empid=emp_id, attachment=file,uploaded_time__month=today.month)
                attachment.attachment = file
                attachment.Plan_forthe_Next_Month = plan_for_next_month
                attachment.remarks = remarks
                attachment.save()
            except Attachment.DoesNotExist:
                # Create a new attachment if none exists
                Attachment.objects.create(
                    empid=emp_id,
                    attachment=file,
                    Plan_forthe_Next_Month=plan_for_next_month,
                    remarks=remarks
                )

        success_message = "Files uploaded successfully"

    return render(request, 'people_trained.html', {'success_message': success_message})

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Attachment

def delete_attachment(request, attachment_id):
    if request.method == 'POST':
        attachment = get_object_or_404(Attachment, id=attachment_id)
        attachment.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def editfield(request, empid, form_number):


    
    a = FormData.objects.filter(empid=str(empid), form_number=int(form_number)).first()
    if a:
        loc = None
        div = None

        if a:
            emp_id = a.empid
            loc = a.location
            div = a.division

        print(div)
        Locations=Show.objects.filter(locations=loc, divisions= div)
        list_values = []

        for location in Locations:
            titles = location.list.all()  # Retrieve all related Title_Creation objects
            for title in titles:
                list_values.append(title.title_creation)  # Access the specific field of Title_Creation
            
    # Removing duplicates if needed
        list_values = list(set(list_values))
        print(list_values)
        location = Location.objects.all()
        tc = Title_Creation.objects.filter(title_creation__in=list_values).order_by('-id')  # Reverse order by 'id' or any other suitable field
        dc = Title_Creation.objects.filter(title_creation__in=list_values).order_by('-id')  # Reverse order by 'id' or any other suitable field
        values = FormData.objects.filter(empid=emp_id, date = date)
        print(emp_id)
        print(values)
        # Reverse the order of tc queryset
        tc = reversed(tc)
    else:
        return 'invalid id'
    return render(request, 'editfield.html', {'location': location, 'tc': tc,'dc':dc, 'empid':emp_id,'div':div, 'loc':loc,'Locations':Locations, 'values':values})



def get_month_data(request, month):
    # Assuming your model has a field named 'date' which is a DateField or DateTimeField
    existing_entry = FormData.objects.filter(date__month=month)
    data_list = list(existing_entry.values('title_creation', 'field_name', 'field_value', 'division', 'location', 'date'))
    
    return JsonResponse(data_list, safe=False)