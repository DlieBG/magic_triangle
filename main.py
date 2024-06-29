import itertools

def _calc_line_sums(numbers: list[int]) -> tuple[int]:
    _top = numbers[0]
    _mid = numbers[1:((len(numbers) + 6) // 3)]
    _down = numbers[-((len(numbers) + 3) // 3):]

    line_1 = _top + sum(x for i, x in enumerate(_mid) if i % 2 == 0) + _down[0]
    line_2 = _top + sum(x for i, x in enumerate(_mid) if i % 2 == 1) + _down[-1]
    line_3 = sum(_down)
    
    return line_1, line_2, line_3

def _match_lines(lines: tuple[int], target: int) -> bool:
    for line in lines:
        if line != target:
            return False
        
    return True

numbers = [
    int(x) for x in
        input('Input numers to place: ').split(
            sep=' ',
        )
]
target = int(input('Target sum: '))

print('Triangle width is', (len(numbers) + 3) // 3)

for permutation in itertools.permutations(numbers):
    if _match_lines(
        lines=_calc_line_sums(
            numbers=permutation,
        ),
        target=target,
    ):
        _top = permutation[0]
        _down = permutation[-((len(permutation) + 3) // 3):]

        print(
            'All lines match the target at this permutation',
            permutation,
            'with this corners',
            (_top, _down[0], _down[-1]),
        )
        break
