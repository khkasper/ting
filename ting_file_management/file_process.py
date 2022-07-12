import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return None

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(info)
    sys.stdout.write(str(info))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    file = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    except IndexError:
        sys.stderr.write("Posição inválida")
