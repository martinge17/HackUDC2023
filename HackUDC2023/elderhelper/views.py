from django.http import HttpResponse
from django.shortcuts import render
import openai

openai.api_key = "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"
model_engine = "text-davinci-003"

def index(request):
    return render(request,'index.html',{})


def generate_text(request):
    if request.method == 'POST':
         input_text = request.POST.get('input_text')
         completion = openai.Completion.create(
             engine=model_engine,
             prompt=input_text,
             max_tokens=1024,
             n=1,
             stop=None,
             temperature=0.5,
         )
         generated_text = completion.choices[0].text
         return render(request, 'output.html', {'generated_text': generated_text})
    return render(request, 'input.html')
