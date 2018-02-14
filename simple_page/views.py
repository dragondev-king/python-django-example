# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import View
from django.shortcuts import render, redirect
import json
import requests

from simple_page.forms import NameForm

class HomePageView(View):
    """Home Page"""

    def get(self, request):
        """Return Form to get GitHub username"""
        form = NameForm()
        return render(request, 'simple_page/enter_user_page.html', {'form': form})

    def post(self, request):
        """
        Expect GitHub username
        Return Formatted GitHub Profile
        """
        form = NameForm(request.POST)
        if form.is_valid():
            data = requests.get('https://api.github.com/users/' + form.cleaned_data['name']).json()
            return render(request, 'simple_page/retrieve_user_page.html', {'data': data, 'json': json.dumps(data, indent=2)})
        else:
            return redirect('home')
