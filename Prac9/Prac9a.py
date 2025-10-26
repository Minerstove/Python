def fizzbuzz(x,y,seq):
    it = iter(seq)
    x, y = str(x), str(y)
    for item in it:
        str_item = str(item)
        if str_item[0] == x and str_item[-1] == y:
            yield "FizzBuzz"
        elif str_item[0] == x:
            yield "Fizz"
        elif str_item[-1] == y:
            yield "Buzz"
        else:
            yield item

assert [*fizzbuzz(3, 5, [31415, 92, 65, 358, 979, 3, 23, 8, 46])] == ['FizzBuzz', 92, 'Buzz', 'Fizz', 979, 'Fizz', 23, 8, 46], [*fizzbuzz(3, 5, [31415, 92, 65, 358, 979, 3, 23, 8, 46])]
assert [*fizzbuzz(3, 5, iter([31415, 92, 65, 358, 979, 3, 23, 8, 46]))] == ['FizzBuzz', 92, 'Buzz', 'Fizz', 979, 'Fizz', 23, 8, 46], [*fizzbuzz(3, 5, iter([31415, 92, 65, 358, 979, 3, 23, 8, 46]))]
