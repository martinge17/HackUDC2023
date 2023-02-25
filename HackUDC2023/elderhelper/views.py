from django.shortcuts import render
import openai

openai.api_key = "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"


def generate_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=input_text,
            max_tokens=60
        )
        generated_text = response.choices[0].text
        return render(request, 'output.html', {'generated_text': generated_text})
    return render(request, 'input.html')
