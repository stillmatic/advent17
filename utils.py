def read_input_txt(day):
    target = f'input/day{day}.txt'
    with open(target) as f:
        return f.read().strip()

def read_input_csv(day):
    import pandas as pd
    target = f'input/day{day}.txt'
    return pd.read_csv(target)

def read_input_tsv(day):
    import pandas as pd
    target = f'input/day{day}.txt'
    return pd.read_tsv(target)
