def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # teste (assertions)
    assert tag_bloco('Incluido com sucesso') == \
        '<div class="success">Incluido com sucesso</div>'
    assert tag_bloco('Impossivel excluir', 'erro') == \
        '<div class="erro">Impossivel excluir</div>'
    print(tag_bloco('bloco'))
