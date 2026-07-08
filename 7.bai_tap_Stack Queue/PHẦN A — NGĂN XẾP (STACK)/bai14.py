def stock_span(gia):

    ngan_xep = []

    span = []

    for i in range(len(gia)):

        while (
            ngan_xep
            and gia[ngan_xep[-1]]
            <= gia[i]
        ):
            ngan_xep.pop()

        if not ngan_xep:
            span.append(i + 1)

        else:
            span.append(
                i - ngan_xep[-1]
            )

        ngan_xep.append(i)

    return span


gia = [
    100,
    80,
    60,
    70,
    60,
    75,
    85
]

print(stock_span(gia))