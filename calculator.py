class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for n in args:
            result *= n
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for index in range(1, len(args)):
            if args[index] == 0:
                continue
            result /= args[index]
        return result
    @staticmethod
    def subtract(*args):
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result