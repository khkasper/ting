def exists_word(word, instance):
    word_list = []
    occurrences = []

    for index, line in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1})

    if len(occurrences) > 0:
        word_list.append({
            "palavra": word,
            "arquivo": instance._data[0]["nome_do_arquivo"],
            "ocorrencias": occurrences,
        })

    return word_list


def search_by_word(word, instance):
    word_list = []
    occurrences = []

    for index, line in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1, "conteudo": line})

    if len(occurrences) > 0:
        word_list.append({
            "palavra": word,
            "arquivo": instance._data[0]["nome_do_arquivo"],
            "ocorrencias": occurrences,
        })

    return word_list
