def function_a():
    x = 10

    def function_b():
        # nonlocal x
        x = 20
        print("function_b",x)

    function_b()
    print("function_a", x)
function_a()

