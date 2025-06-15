from django.shortcuts import render,redirect 
from django.contrib.auth.models import User 
from django.contrib import messages 
from smartcity.models import ServiceProviderR 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect 
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.utils.http import url_has_allowed_host_and_scheme 
from django.utils.http import url_has_allowed_host_and_scheme # Django 4.0+
# Create your views here.
def CustomerReg(request): 
  if request.method=="POST":
     first_name=request.POST.get('first_name')
     last_name=request.POST.get('last_name') 
     username=request.POST.get('username')
     email=request.POST.get('email') 
     password=request.POST.get('password')
    #to check username exists or not 
     user=User.objects.filter(username=username)
     if user.exists(): 
           messages.error(request,'username already exits') 
           return redirect('/CustomerReg/')
     user=User.objects.create( 
         first_name=first_name,
         last_name=last_name,
         username= username, 
         email=email, )
     user.set_password(password) 
     user.save() 
     messages.success(request, 'Acount Created successfully!') 
     return redirect('/CustomerReg/') 
  return  render(request,'CustomerRegister.html') 
#serviceprovider
def ServiceproviderReg(request): 
    if request.method == "POST": 
      service_image = request.FILES.get('service_image')
      first_name = request.POST.get('first_name') 
      last_name =request.POST.get('last_name') 
      username = request.POST.get('username')
      servicename = request.POST.get('servicename') 
      email = request.POST.get('email')
      Phoneno = request.POST.get('Phoneno')
      password = request.POST.get('password')
      address = request.POST.get('address') 
      # Check if username exists 
      if User.objects.filter(username=username).exists(): 
        messages.error(request,'Username already exists') 
        return redirect('/ServiceproviderReg/')
       #Create theUser instance
      user = User.objects.create_user( 
         first_name=first_name,
         last_name=last_name, 
         username=username, 
         email=email, )
         # Hash the password 
      user.set_password(password)
      user.save()
     # Create the ServiceProviderR instance 
    service_provider = ServiceProviderR( 
         user=user,
         service_image=service_image, 
         servicename=servicename,
         Phoneno=Phoneno,
         address=address, ) 
    service_provider.save() 
    messages.success(request, 'Service provider registered successfully!') 
    return redirect('/ServiceproviderReg/')
    return render(request, 'ServiceProviderR.html')
#login logic 
def Login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect(f'/Login_page/?next={next_url}' if next_url else '/Login_page/')
        else:
            login(request, user)
            messages.success(request, 'Login successful!')
            
            # Updated safe URL check
            if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure()
            ):
                return redirect(next_url)
            
            try:
                ServiceProviderR.objects.get(user=user)
                return redirect('/ServiceproviderReg/')
            except ServiceProviderR.DoesNotExist:
                return redirect('/Plumber/')
    
    # GET request handling
    next_url = request.GET.get('next', '')
    return render(request, 'login_page.html', {'next_url': next_url})
#Home section
@login_required(login_url='/Login_page/') 
def Plumber(request): 
# Start with base queryset for plumbers 
   queryset = ServiceProviderR.objects.filter(
   servicename__iexact='plumber' ).select_related('user')
# Get search parameter from the request 
   location = request.GET.get('location', '').strip() 
   # Start with base queryset 
   if location: 
      # If location is provided, get all plumbers in that  location
       queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='plumber').select_related('user') 
       page_title = f"Plumbers in {location}" 
   else: 
   # If nolocation provided, show all plumbers 
     queryset = ServiceProviderR.objects.filter(servicename__iexact='plumber').select_related('user')
     page_title = "Professional Plumbers" 
     context = { 'plumbers': queryset,'page_title': page_title, 'search_location': location, }
     return render(request,'Plumber.html', context) 
def Home(request): 
 return render(request,'home.html') 
@login_required 
def logout_view(request): 
   logout(request) 
   #Redirect to your desired page after logout 
   return redirect('/Home/')
@login_required(login_url='/Login_page/') 
def electrition(request): 
  #Start with base queryset for electrition 
   queryset = ServiceProviderR.objects.filter( servicename__iexact='electrition').select_related('user') 
   #Get search parameter from the request 
   location =request.GET.get('location', '').strip() 
   # Start with base queryset 
   if location:
   #If location is provided, get all electrition in that location 
     queryset =ServiceProviderR.objects.filter( address__icontains=location,servicename__iexact='electrition').select_related('user')
     page_title = f"Electrition in {location}" 
   else: 
     #If no location provided, show all electrition 
     queryset = ServiceProviderR.objects.filter(servicename__iexact='electrition').select_related('user')
     page_title = "Professional electrition" 
     context = { 'electritions': queryset, 'page_title': page_title, 'search_location': location, } 
     return render(request,'Electrition.html',context)
@login_required(login_url='/Login_page/') 
def carpenter(request): 
        #Start with base queryset for plumbers 
        queryset = ServiceProviderR.objects.filter(servicename__iexact='carpenter' ).select_related('user') 
        # Get search parameter from the request 
        location = request.GET.get('location', '').strip() 
        # Start with base queryset 
        if location: 
        # If location is provided, get all carpenters in that location 
             queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='carpenter'  ).select_related('user') 
             page_title = f"Carpenter in {location}"
        else:
        # If no location provided, show all carpenter 
          queryset =ServiceProviderR.objects.filter( servicename__iexact='carpenter').select_related('user') 
          page_title = "Professional carpenter" 
          context= { 'carpenters': queryset, 'page_title': page_title, 'search_location':location, } 
          return render(request,'Carpenter.html',context)
@login_required(login_url='/Login_page/') 
def painters(request): 
      #Start with base queryset for painters 
      queryset = ServiceProviderR.objects.filter(servicename__iexact='painter' ).select_related('user') 
      #Get search parameter From the request 
      location = request.GET.get('location', '').strip() 
      #Start with base queryset 
      if location: 
      #If location is provided, get all painters in that location 
        queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='painter').select_related('user')
        page_title = f"painter in {location}" 
      else:
       #if no lcation provided, show all painters 
       queryset = ServiceProviderR.objects.filter(servicename__iexact='painter').select_related('user')
       page_title = "Professional Painters" 
       context = { 'painters': queryset,'page_title': page_title, 'search_location': location, } 
       return render(request,'Painters.html',context)
#for weldingwork
@login_required(login_url='/Login_page/') 
def welding(request): 
    #Start with base queryset for welding 
    queryset = ServiceProviderR.objects.filter(servicename__iexact='welding' ).select_related('user') 
    # Get search parameter from the request
    location = request.GET.get('location', '').strip() 
    #Start with base queryset 
    if location: 
      # If location is provided, get all welding in that location
       queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='welding').select_related('user') 
       page_title = f"Welding in {location}" 
    else: 
      #If no location provided, show all welding
      queryset = ServiceProviderR.objects.filter(servicename__iexact='welding').select_related('user')
      page_title = "Professional Welders" 
      context = { 'welding': queryset,'page_title': page_title, 'search_location': location, } 
      return render(request,'Weldingwork.html',context) 
#for cableprovider
@login_required(login_url='/Login_page/') 
def Cableprovider(request): 
      #Start with base queryset for cableprovider 
      queryset = ServiceProviderR.objects.filter(servicename__iexact='cableprovider' ).select_related('user') 
      #Get search parameter from the request 
      location = request.GET.get('location', '').strip() 
      #Start with base queryset 
      if location: 
          # f location is provided, get all cableprovider in that location 
          queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='cableprovider' ).select_related('user') 
          page_title = f"CableProvider in {location}"
      else: 
       #If no location provided, show all cableprovider  
       queryset =ServiceProviderR.objects.filter( servicename__iexact='cableprovider').select_related('user') 
       page_title = "Professional CableProvider"
       context = { 'Cableprovider': queryset, 'page_title': page_title,'search_location': location, } 
       return render(request,'Cableprovider.html',context)
@login_required(login_url='/Login_page/') 
def Internet(request): 
      # Start with base queryset for Internet 
      queryset = ServiceProviderR.objects.filter(servicename__iexact='Internet' ).select_related('user') 
      # Get search parameter from the request 
      location = request.GET.get('location', '').strip() 
      # Start with base queryset 
      if location: 
        # If location is provided, get all internet in that location 
        queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='Internet').select_related('user') 
        page_title = f"Internet in {location}" 
      else:
           # If no location provided, show all internet 
           queryset = ServiceProviderR.objects.filter(servicename__iexact='Internet').select_related('user')
           page_title = "Professional Internet" 
           context = { 'Internet': queryset,'page_title': page_title, 'search_location': location, } 
           return render(request,'Internet.html',context)
@login_required(login_url='/Login_page/') 
def Groceries(request): 
     #Start with  base queryset for groceries 
     queryset = ServiceProviderR.objects.filter(servicename__iexact='Groceries' ).select_related('user') 
     #Get search parameter from the request 
     location = request.GET.get('location', '').strip() 
     #Start with base queryset 
     if location: 
       #If location is provided, get all groceries in that location 
       queryset = ServiceProviderR.objects.filter(address__icontains=location, servicename__iexact='Groceries').select_related('user') 
       page_title = f"Groceris in {location}" 
     else: 
          #If no location provided, show all groceries 
          queryset =ServiceProviderR.objects.filter( servicename__iexact='Groceries' ).select_related('user') 
          page_title = "Professional Groceries" 
          context= { 'Groceries': queryset, 'page_title': page_title, 'search_location':location, } 
          return render(request,'Grocries.html',context)
