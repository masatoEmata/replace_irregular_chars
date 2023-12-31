from .utils import replace_pair

SOUND_SYMBOL_VARIATIONS = [
    ("ヴ", "ヴ"),
    ("ガ", "ガ"),
    ("ギ", "ギ"),
    ("グ", "グ"),
    ("ゲ", "ゲ"),
    ("ゴ", "ゴ"),
    ("が", "が"),
    ("ぎ", "ぎ"),
    ("ぐ", "ぐ"),
    ("げ", "げ"),
    ("ご", "ご"),
    ("ざ", "ざ"),
    ("じ", "じ"),
    ("ず", "ず"),
    ("ぜ", "ぜ"),
    ("ぞ", "ぞ"),
    ("ザ", "ザ"),
    ("ジ", "ジ"),
    ("ズ", "ズ"),
    ("ゼ", "ゼ"),
    ("ゾ", "ゾ"),
    ("だ", "だ"),
    ("ぢ", "ぢ"),
    ("づ", "づ"),
    ("で", "で"),
    ("ど", "ど"),
    ("ダ", "ダ"),
    ("ヂ", "ヂ"),
    ("ヅ", "ヅ"),
    ("デ", "デ"),
    ("ド", "ド"),
    ("ば", "ば"),
    ("ぱ", "ぱ"),
    ("び", "び"),
    ("ぴ", "ぴ"),
    ("ぶ", "ぶ"),
    ("ぷ", "ぷ"),
    ("べ", "べ"),
    ("ぺ", "ぺ"),
    ("ぼ", "ぼ"),
    ("ぽ", "ぽ"),
    ("バ", "バ"),
    ("パ", "パ"),
    ("ビ", "ビ"),
    ("ピ", "ピ"),
    ("ブ", "ブ"),
    ("プ", "プ"),
    ("ベ", "ベ"),
    ("ペ", "ペ"),
    ("ボ", "ボ"),
    ("ポ", "ポ"),
]


def combine_sound_symbols(text: str) -> str:
    """
    >>> combine_sound_symbols("ガギグゲゴ")
    'ガギグゲゴ'
    >>> combine_sound_symbols("がぎぐげご")
    'がぎぐげご'
    """
    return replace_pair(text, SOUND_SYMBOL_VARIATIONS)
