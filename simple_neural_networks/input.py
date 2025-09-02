def clearing_input(_input: str):
    # Очистка двойных и более пробелов
    _input.strip()
    while "  " in _input:
        _input.replace("  ", " ")
    