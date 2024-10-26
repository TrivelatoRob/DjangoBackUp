from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Courses
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CoursesListView(View):
    # Listar todos os cursos
    def get(self, request):
        courses = list(Courses.objects.values())
        return JsonResponse(courses, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CoursesCreateView(View):
    def post(self, request):
        data = json.loads(request.body)

        # Validação manual
        errors = {}
        if 'name' not in data or not data['name']:
            errors['name'] = "Este campo é obrigatório."
        if 'professor' not in data or not data['professor']:
            errors['professor'] = "Este campo é obrigatório."
        if 'description' not in data or not data['description']:
            errors['description'] = "Este campo é obrigatório."
        elif Courses.objects.filter(name=data['name']).exists():
            errors['name'] = "Este curso já está cadastrado."
    

        if errors:
            return JsonResponse(errors, status=400)

        # Criar o estudante
        courses = Courses.objects.create(
            name=data['name'],
            professor=data['professor'],
            description=data['description'],
        )

        # Assumindo que 'courses' é uma lista de IDs
        if 'courses' in data:
            courses.courses.set(data['courses'])

        return JsonResponse({'id': courses.id}, status=201)



@method_decorator(csrf_exempt, name='dispatch')
class CoursesDetailView(View):
    # Ver detalhes de um estudante específico, atualizar e deletar
    def get(self, request, courses_id):
        courses = get_object_or_404(Courses, id=courses_id)
        data = {
            'id': courses.id,
            'name': courses.name,
            'professor': courses.professor,
            'description': courses.description,
        }
        return JsonResponse(data)

    def put(self, request, courses_id):
        courses = get_object_or_404(Courses, id=courses_id)
        data = json.loads(request.body)

        # Validação manual
        errors = {}
        
        # Validação somente se o campo estiver presente na requisição
        if 'name' in data:
            if data['name'] == "":
                errors['name'] = "Este campo não pode ser vazio."

        if 'professor' in data:
            if data['professor'] == "":
                errors['professor'] = "Este campo não pode ser vazio."

        if 'description' in data:
            if data['description'] == "":
                errors['description'] = "Este campo não pode ser vazio."

        if errors:
            return JsonResponse(errors, status=400)

        # Atualizar apenas os campos fornecidos
        if 'name' in data:
            courses.name = data['name']
        if 'professor' in data:
            courses.professor = data['professor']
        if 'description' in data:
            courses.description = data['description']
        
        courses.save()

        return JsonResponse({'id': courses.id}, status=200)

    def delete(self, request, courses_id):
        courses = get_object_or_404(Courses, id=courses_id)
        courses.delete()
        return JsonResponse({'message': 'course deleted'}, status=204)