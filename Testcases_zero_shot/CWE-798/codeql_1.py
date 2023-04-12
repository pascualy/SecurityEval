def process_request(request):
    expected_password = "my_password"
    password = request.GET.get('password')
    if password == expected_password:
        return redirect('login')
    else:
        return HttpResponse('Incorrect password')