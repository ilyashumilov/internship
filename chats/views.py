from django.shortcuts import render
from utils import create_new_chat


class View:
    def get(self):
        create_new_chat()
# Create your views here.
