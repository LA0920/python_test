def in_autotests_we_trust(a: object, b: object) -> None:
    """

    :rtype: object
    """
    if a == b:
        print('Test passed')
    else:
        print('Test failed')


in_autotests_we_trust(10, '10')
in_autotests_we_trust(0, False)
