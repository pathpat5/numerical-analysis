# for n = 1:5
#     x = n * 0.1;
#     z = myfunc2(x, 2.3, 7);
#     fprintf('x = %4.2f f(x) = %8.4f \r', x, z);
# end

'''
    it prints the values of `x` and `z` using the `fprintf` function. 
    The format string `'x = %4.2f f(x) = %8.4f \r'` 
    specifies that `x` should be printed as a floating-point number with 4 characters wide and 2 decimal places,
    and `z` should be printed as a floating-point number with 8 characters wide and 4 decimal places. 
    The `\r` at the end of the format string causes the cursor to return to the beginning of the line after each iteration, 
    so that the output of the next iteration overwrites the previous one.
'''