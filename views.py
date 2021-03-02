from utils import load_data, load_template, build_response
from urllib.parse import unquote_plus
import json
from database import Database, Note


DB_NAME = "notes"
db = Database(DB_NAME)


def get_note_from_post(corpo):
    note = []
    for chave_valor in corpo.split('&'):
        split = chave_valor.split('=')
        key = unquote_plus(split[0])
        value = unquote_plus(split[1])
        note.append(value)
    return Note(None, note[0], note[1])


def index(request):
    notes_list = db.get_all()
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        note = get_note_from_post(corpo)
        db.add(note)
        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in notes_list
    ]
    notes = '\n'.join(notes_li)

    return build_response() + load_template('index.html').format(notes=notes).encode()
