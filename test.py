import flet as ft
from datetime import datetime
def main_page(page:ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value='Привет, как тебя зовут?')

    greeting_history = []
    history_text = ft.Text('История приветствий')
    like_list = []
    like_text = ft.Text(value='избранные')

    page.theme_mode = ft.ThemeMode.LIGHT

    def on_button_click(_):
        name = name_input.value.strip()

        print(greeting_text.value)
        greeting_text.value = f'Привет{name}'
        print(greeting_text.value)

        if name:
            greeting_text.color = None
            greeting_text.value = f'Привет {name}'
            name_input.value = None

            timestamp = datetime.now().strftime("%d:%m:%y  " "  %H:%M:%S" )
            greeting_history.append(f'{timestamp} {name}')
            history_text.value ='история приветсвий \n' + '\n'.join(greeting_history)


            if len(greeting_history) >4:
                greeting_history.pop(-5)
            else:
                None
        else:
            greeting_text.value = 'Введите возраст!'
            greeting_text.color = ft.Colors.RED    

        

        page.update()

            
    name_input = ft.TextField(label='введите имя' , on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon =ft.Icons.SEND_ROUNDED , on_click=on_button_click)

    def theme_mode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_mode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6 , on_click=theme_mode)

    def clear_history(_):
        greeting_history.clear()
        history_text.value =('история приветсвий')
        page.update()

    def on_click_like(_):
            like_list.append(f'{greeting_history[-1]}')
            like_text.value = 'избранные\n' + '\n'.join(like_list)
            page.update()


    clear_button = ft.ElevatedButton(text='clear' , icon=ft.Icons.DELETE , on_click=clear_history)
    like_button = ft.ElevatedButton("like",on_click=on_click_like)

    page.add(greeting_text , name_input , input_button_text ,theme_mode_button, clear_button,like_button, history_text , like_text  )


    
ft.app(target=main_page)