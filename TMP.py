text = 'Django+GO!+Text.'
spl = len(text.split('+'))
print(spl)


def reverse(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    ln = len(user_text.split('+'))

    return render(request, 'reverse.html', {'usertext': user_text,
                                            'reversetext': reverse_text, }
    'ln': ln, )
