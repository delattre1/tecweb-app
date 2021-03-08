import os
import json
from urllib.parse import unquote_plus
from database import Note


def extract_route(request):
    route_args = request.split()[1][1:]
    route_args_split = route_args.split('?')
    try:
        args = route_args_split[1]
        note_id = args.split('=')[1]
    except:
        note_id = None

    route = route_args_split[0]
    print(f'rota: {route_args_split}, idNote: {note_id}\n')
    return route, note_id


def read_file(path):
    extension = os.path.splitext(path)[1]
    format_text = ['.txt', '.html', '.js', '.css']
    if extension in format_text:
        #print(f'\nfilepath: {path} {extension}\n')
        with open(path, 'rt') as file:
            return file.read()

    with open(path, 'rb') as file:
        return file.read()


def load_data(json_path):
    with open('data/' + json_path) as json_file:
        data = json.load(json_file)
        return data


def load_template(template_file):
    return read_file('templates/' + template_file)


def build_response(body='', code='200', reason='OK', headers=''):
    args = [str(code), reason]
    response = 'HTTP/1.1 ' + (' '.join(args))
    if headers == '':
        response += '\n\n' + body
    else:
        response += '\n' + headers + '\n\n' + body
    return response.encode()


def get_note_from_post(corpo):
    note = []
    for chave_valor in corpo.split('&'):
        split = chave_valor.split('=')
        key = unquote_plus(split[0])
        value = unquote_plus(split[1])
        note.append(value)

    return Note(note[0], note[1], note[2])


def verify_and_delete(body_request, database):
    body_split = body_request.split('=')
    if body_split[0] == 'deleteNote':
        database.delete(body_split[1])
        return True
