
from django.shortcuts import render, redirect
import pickle

# Create your views here.
def index(request):
    context = {
        "answer" : "Try Adding values"
    }
    print('Hello world')
    if request.method == 'POST':
        erStatus = float(request.POST.get('erStatus'))
        prStatus = float(request.POST.get('prStatus'))
        herstatus = float(request.POST.get('herstatus'))
        print(f'${erStatus} ${prStatus} ${herstatus}')

        # Load the model from the pickle file
        with open('accounts/model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        input = erStatus, prStatus, herstatus
        y_pred = model.predict([input])
        if y_pred == 0 :
            ans = "No Triple Negative Breast Cancer"
            print("No Triple Negative")
        else :

            ans ="Triple Negative Breast Cancer"
            print("Triple Negative")

        context = {
        "answer" : ans
        }




    return render(request, 'new.html', context=context)

