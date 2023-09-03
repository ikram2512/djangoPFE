from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'myApp/home.html')

def upload_images(request):
    if request.method == 'POST':
        single_image = request.FILES.get('single-image')
        multiple_images = request.FILES.getlist('multiple-images')
        
        # Vous pouvez maintenant enregistrer les images ou effectuer d'autres actions
    return render(request, 'myApp/upload_image.html')

def scanner_page(request):
    if request.method == 'POST':
        # Traitez le formulaire ici
        pass
        
    return render(request, 'myApp/scanner_page.html')

def scan_single_document(request):
    if request.method == 'POST' and request.FILES.get('single-document'):
        single_document = request.FILES['single-document']
        # Traitez le scan du document ici
        
    return render(request, 'myApp/scanner_page.html')

def scan_multiple_documents(request):
    if request.method == 'POST' and request.FILES.getlist('multiple-documents'):
        multiple_documents = request.FILES.getlist('multiple-documents')
        # Traitez le scan des documents multiples ici
        
    return render(request, 'myApp/scanner_page.html')




        
    