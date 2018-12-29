def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # teste (assertions)
    assert tag_bloco('Incluindo com sucesso') == \
        '<div class="success">Incluido com sucesso</div>'
