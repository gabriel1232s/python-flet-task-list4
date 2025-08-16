# import flet as ft

# def main(page: ft.Page):
#     tarefa_input = ft.TextField(label="Nova tarefa", width=300)
#     lista = ft.Column()

#     def adicionar(e):
#         if tarefa_input.value.strip():
#             lista.controls.append(ft.Text(f"✅ {tarefa_input.value}"))
#             tarefa_input.value = ""
#             page.update()

#     page.add(
#         tarefa_input,
#         ft.ElevatedButton("Adicionar", on_click=adicionar),
#         lista
#     )

# ft.app(target=main)

   
import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"

    tarefa_input = ft.TextField(label="Nova tarefa", width=300)
    lista = ft.Column()

    def adicionar(e):
        if tarefa_input.value.strip():
            # Criar a checkbox para a tarefa
            tarefa = ft.Checkbox(label=tarefa_input.value)
            
            # Adicionar a checkbox à lista
            lista.controls.append(tarefa)
            
            tarefa_input.value = ""
            page.update()

    page.add(
        tarefa_input,
        ft.ElevatedButton("Adicionar", on_click=adicionar),
        lista
    )

ft.app(target=main)
