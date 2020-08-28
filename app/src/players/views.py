from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import *

from .forms import BasicUserForm, PlayerForm, CubeForm

## Players
def PlayerCreateView(request):
    if request.method == "POST":
        user_form = BasicUserForm(request.POST)
        player_form = PlayerForm(request.POST)

        if user_form.is_valid() and player_form.is_valid():
            user_form.save()
            user_form.user = user
            player_form.save()
            return redirect('home')
    else:
        user_form = BasicUserForm()
        player_form = PlayerForm()

    context =  {'user_form': user_form, 'player_form': player_form}
    return render(request, 'signup.html', context)


class PlayerProfileView(ListView):
    model = Cube
    template_name = "login.html"

     #def get_querySet(self):
     #   return Player.objects.filter()

    def get_querySet(self):
        return Player.objects.filter()


## Cubes
class CubeCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = { 'form': CubeForm() }
        return render(request, 'register_cube.html', context)

    def post(self, request, *args, **kwargs):
        print('Cube DataForm -> ', request.POST)
        print('Cube FilesForm ->', request.FILES)
        # form =  CubeForm(request.POST)  Use this if is only data
        form = CubeForm(request.POST, request.FILES)
        print('{} -> {}'.format(form.is_valid(), form.errors))
        if form.is_valid():
            cube = form.save()
            return redirect(reverse_lazy('list_cubes'))
        return render(request, 'register_cube.html', {'form': form})

class CubeListView(ListView):
    model = Cube
    template_name = "list_cubes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Solved Cubes'
        print('Print Content ->', context)
        return context

class CubeDetailView(DetailView):
    model= Cube

    def get(self, request, *args, **kwargs):
        cube = get_object_or_404(Cube, pk=kwargs['id'])
        context = {'cube': cube}
        return render(request, 'cube_detail.html', context)

class CubeUpdateView(UpdateView):
    model = Cube
    form_class = CubeForm
    template_name = 'cube_update.html'
    success_url = reverse_lazy('list_cubes')

    ## Options
    # fields = '__all__' without form
    # template_name_suffix = '_update' option to find the template

    # def get(self, request, *args, **kwargs):
    #     self.object = Cube.objects.get(cube_id=kwargs['id'])
    #     self.form_class = self.get_form(self.form_class)
    #     context = self.get_context_data(object=self.object, form=self.form_class)
    #     return self.render_to_response(context)

    # def post(self, request, *args, **kwargs):
    #     print('THIS IS A POST -> ', request.POST)
    #     form = CubeForm(request.POST, request.FILES)
    #     print('{} -> {}'.format(form.is_valid(), form.errors))
    #     if form.is_valid():
    #         cube = form.save() could use force_update=True
    #         self.object = cube
    #     return render(request, 'cube_detail.html', {'cube': self.object})

    # def get_object(self, queryset=None):
    #     return Cube.objects.get(cube_id=kwargs['id'])

class CubeDeleteView(DeleteView):
    model = Cube
    template_name = 'delete_cube.html'
    success_url = reverse_lazy('list_cubes')


## Test Views based in functions
def infoHttpView(request):
    http_object = """<h1> Test Route</h2>
    <p>This is a example of view based in function with HttpResponse</p>
    <p>Remember the context view</p>
    """
    return HttpResponse(http_object)

def infoJsonView(request):
    json_object = {
        'title': 'Test Route',
        'code': 200,
        'message': 'Example of view based in function with JsonResponse'
    }
    return JsonResponse(json_object)

def infoJsonParamView(request, param=False):
    json_object = {
        'title': 'Test Param Route',
        'code': 200
    }
    success_msg = 'Example JsonResponse with param -> {}'.format(param)
    json_object['message'] = success_msg if param else 'THIS WONT NEVER SEE, PARAM COMPROVED IN ROUTE'
    return JsonResponse(json_object)
